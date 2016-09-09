from Implementation import NowServing

from bhive.environment.bhive_integration import BHiveIntegration

def before_all(context):
    BHiveIntegration.before_all(context)
    context.machine = NowServing.NowServing()


def after_all(context):
    BHiveIntegration.after_all(context)


def before_feature(context, feature):
    BHiveIntegration.before_feature(context, feature)


def after_feature(context, feature):
    BHiveIntegration.after_feature(context, feature)


def before_scenario(context, scenario):
    BHiveIntegration.before_scenario(context, scenario)


def after_scenario(context, scenario):
    BHiveIntegration.after_scenario(context, scenario)


def before_step(context, step):
    BHiveIntegration.before_step(context, step)


def after_step(context, step):
    BHiveIntegration.after_step(context, step)


def before_tag(context, tag):
    BHiveIntegration.before_tag(context, tag)


def after_tag(context, tag):
    BHiveIntegration.after_tag(context, tag)
