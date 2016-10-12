from behave import given, when, then

from bhive.integration import log_info, declare_variable


@given(u'Machine is off')
def step_impl(context):
    declare_variable(context, 'running', 'BOOL', 'FALSE')
    declare_variable(context, 'display', 'INT', '0')
    context.state.ensure_that('running','=','FALSE')


@when(u'Machine is started')
def step_impl(context):
    # this is the assignment state change
    context.state.assign([('running', ':=', 'TRUE')])
    context.state.assign([('display', ':=', '1')])


@then(u'Machine is on')
def step_impl(context):
    context.state.test_that(context, 'running', '=', 'TRUE')
    pass

@then(u'Display should show 1')
def step_impl(context):
    context.state.test_that(context, 'display', '=', 1)
    pass

# @then(u'The next ticket should be 1')
# def step_impl(context):
#     # bhive needs to know what?  this is an assertion of the machine state
#     assert context.machine.take_ticket() == 1
#
#
# @then(u'The "Now Serving" display should be blank')
# def step_impl(context):
#     assert context.machine.display == ''
#
# @given(u'Machine is on')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given Machine is on')
#
#
# @when(u'A ticket is dispensed')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When A ticket is dispensed')
#
#
# @then(u'The ticket should be less than the displayed number')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then The ticket should be less than the displayed number')
#
#
# @given(u'Wicket <wicket> is open')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given Wicket <wicket> is open')
#
#
# @when(u'Wicket <wicket> serves a customer with ticket <ticket>')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When Wicket <wicket> serves a customer with ticket <ticket>')
#
#
# @then(u'The "Now Serving" display should show <wicket> is serving <ticket>')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then The "Now Serving" display should show <wicket> is serving <ticket>')
#
#
# @when(u'Wicket <wicket> is closed')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When Wicket <wicket> is closed')
#
#
# @then(u'The "Now Serving" display should now show <wicket>')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then The "Now Serving" display should now show <wicket>')
#
#
# @when(u'Machine is stopped')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When Machine is stopped')
#
#
# @then(u'Machine is off')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Machine is off')
