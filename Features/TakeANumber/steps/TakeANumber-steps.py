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
    context.state.test_that(context, 'display', '=', '1')

@then(u'Ticket is 1')
def step_impl(context):
    context.state.test_that(context, 'ticket', '=', '1')

@given(u'Machine is on')
def step_impl(context):
    context.state.ensure_that('running', '=', 'TRUE')

@when(u'Machine is stopped')
def step_impl(context):
    context.state.assign([('running', ':=', 'FALSE')])
    context.state.assign([('display', ':=', '0')])

@then(u'Machine is off')
def step_impl(context):
    context.state.test_that(context, 'running', '=', 'FALSE')

@then(u'Display shows 0')
def step_impl(context):
    context.state.test_that(context, 'display', '=', '0')

@when(u'Customer takes <ticket>')
def step_impl(context):
    context.state.assign([('ticket', ':=', 'ticket + 1')])

@then(u'Display should be less than or equal to the ticket')
def step_impl(context):
    context.state.test_that(context, 'display', '<=', 'ticket')
    context.state.test_that_always(context, 'display', '<=', 'ticket')

@given(u'Display is less than <ticket>')
def step_impl(context):
    context.state.ensure_that('display', '<', 'ticket')

@when(u'A customer is called')
def step_impl(context):
    context.state.assign([('display', ':=', 'display + 1')])

@when(u'Machine is reset')
def step_impl(context):
    context.state.assign([('display', ':=', '1')])
    context.state.assign([('ticket', ':=', '1')])

