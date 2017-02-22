import bhive
import bhive.integration

from  Implementation import NowServingModel


def before_all(context):
    bhive.integration.before_all(context)


def after_all(context):
    bhive.integration.after_all(context)


def before_feature(context, feature):
    bhive.integration.before_feature(context, feature)


def after_feature(context, feature):
    bhive.integration.after_feature(context, feature)


def before_scenario(context, scenario):
    bhive.integration.before_scenario(context, scenario)
    context.domain_model = NowServingModel.TicketingModel()


def after_scenario(context, scenario):
    bhive.integration.after_scenario(context, scenario)


def before_step(context, step):
    bhive.integration.before_step(context, step)


def after_step(context, step):
    bhive.integration.after_step(context, step)
