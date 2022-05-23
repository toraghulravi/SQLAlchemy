from functools import wraps
from sqlalchemy.orm import Session

def transcation_isolation(func):
    @wraps(func)
    def func_wrapper(self, *args, **kwargs):
        if self.engine is None:
            return func(self, *args, **kwargs, session=session)

        with Session(self.engine) as session:
            return func(self, *args, **kwargs, session=session)
    return func_wrapper
