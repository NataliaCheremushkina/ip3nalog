from .models import Block
from .forms import FeedbackForm


def context_data(request):
    return {
        'feedback_form': FeedbackForm(),
        'blocks': Block.visible_block.all(),
        'menu_blocks': Block.visible_menu.all(),
    }
