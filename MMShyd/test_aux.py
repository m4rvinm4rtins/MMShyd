print('from . import _aux #[ok]')
from . import _aux #[ok]

print('from ._aux import mod2 #[ok]')
from ._aux import mod2 #[ok]
