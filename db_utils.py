from contextlib import contextmanager
from functools import wraps
from typing import Any, Callable, Generator

from sqlalchemy.orm import Session

@contextmanager
def session_scope() -> Generator[Session, None, None]:
    """Provide a transactional scope around a series of operations."""
    session: Session = db_session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def with_session(func: Callable) -> Callable[[], Any]:
    @wraps(func)
    def decorator(*args: Any, **kwargs: Any) -> Any:
        session: Session = db_session()
        try:
            return_value = func(*args, session=session, **kwargs)
            session.commit()
            return return_value
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    return decorator