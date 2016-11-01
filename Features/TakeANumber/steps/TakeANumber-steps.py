from behave import given, when, then

from bhive.integration import log_info, declare_variable

@given(u'Machine is off')
def step_impl(context):
    declare_variable(context, 'running', 'BOOL', 'FALSE')
    declare_variable(context, 'display', 'INT', '0')
    declare_variable(context, 'ticket', 'INT', '0')
    context.state.ensure_that('running','=','FALSE')

@when(u'Machine is started')
def step_impl(context):
    context.state.assign([('running', ':=', 'TRUE')])
    context.state.assign([('display', ':=', '1')])
    context.state.assign([('ticket', ':=', '1')])

@then(u'Machine is on')
def step_impl(context):
    context.state.test_that(context, 'running', '=', 'TRUE')

@then(u'Display shows 1')
def step_impl(context):
    context.state.test_that(context, 'display', '=', 1)

@then(u'Ticket is 1')
def step_impl(context):
    context.state.test_that(context, 'ticket', '=', 1)

@given(u'Machine is on')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Machine is on')

@when(u'Machine is stopped')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Machine is stopped')

@then(u'Machine is off')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Machine is off')

@then(u'Display shows 0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Display shows 0')

@when(u'Customer takes <ticket>')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Customer takes <ticket>')

@then(u'<ticket> should be less than or equal to the display')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then <ticket> should be less than or equal to the display')

@given(u'Display is less than <ticket>')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Display is less than <ticket>')

@when(u'A customer is called')
def step_impl(context):
    raise NotImplementedError(u'STEP: When A customer is called')

@then(u'Display should increase by 1')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Display should increase by 1')

@when(u'Machine is reset')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Machine is reset')

# @given(u'Machine is on')
# def step_impl(context):
#     context.state.ensure_that('running', '=', 'TRUE')
#
#
# @when(u'Machine is stopped')
# def step_impl(context):
#     context.state.assign([('running', ':=', 'FALSE')])
#
#
# @then(u'Machine is off')
# def step_impl(context):
#     context.state.test_that(context, 'running', '=', 'TRUE')
#
# @then(u'Display should be empty')
# def step_impl(context):
#     pass

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
