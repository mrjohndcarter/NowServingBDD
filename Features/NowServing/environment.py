from Implementation import NowServing


def before_all(context):
    context.machine = NowServing.NowServing()
