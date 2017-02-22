from behave import given, when, then

from bhive.integration import log_info, declare_variable

@given(u'Machine is off')
def step_impl(context):
    # start bhive
    declare_variable(context, 'running', 'BOOL', 'FALSE')
    context.state.ensure_that(context, 'running','=','FALSE')
    # end bhive
    context.domain_model.running = False

@when(u'Machine is started')
def step_impl(context):
    # start bhive
    declare_variable(context, 'display', 'INT', '0')
    declare_variable(context, 'ticket', 'INT', '0')
    context.state.assign([('running', ':=', 'TRUE')])
    context.state.assign([('display', ':=', '0')])
    context.state.assign([('ticket', ':=', '1')])
    # end bhive
    context.domain_model.start()

@then(u'Machine is on')
def step_impl(context):
    # start bhive
    context.state.test_that(context, 'running', '=', 'TRUE')
    # end bhive
    assert(context.domain_model.running is True)

@then(u'Display shows 0')
def step_impl(context):
    # start bhive
    context.state.test_that(context, 'display', '=', '0')
    # end bhive
    assert(context.domain_model.display == 0)

@then(u'Ticket is 1')
def step_impl(context):
    # start bhive
    context.state.test_that(context, 'ticket', '=', '1')
    # end bhive
    assert(context.domain_model.ticket == 1)

@given(u'Machine is on')
def step_impl(context):
    # start bhive
    context.state.ensure_that(context, 'running', '=', 'TRUE')
    # end bhive
    context.domain_model.running = True

@when(u'Machine is stopped')
def step_impl(context):
    # start bhive
    context.state.assign([('running', ':=', 'FALSE')])
    context.state.assign([('display', ':=', '0')])
    # end bhive
    context.domain_model.stop()

@then(u'Machine is off')
def step_impl(context):
    # start bhive
    context.state.test_that(context, 'running', '=', 'FALSE')
    # end bhive
    assert(context.domain_model.running is False)

@when(u'Customer takes <ticket>')
def step_impl(context):
    # start bhive
    context.state.assign([('ticket', ':=', 'ticket + 1')])
    # end bhive
    context.domain_model.take_ticket()

@then(u'Display should be less than or equal to the ticket')
def step_impl(context):
    # start bhive
    context.state.test_that(context, 'display', '<=', 'ticket')
    context.state.test_that_always(context, 'display', '<=', 'ticket')
    # end bhive
    assert(context.domain_model.display <= context.domain_model.ticket)

@given(u'Display is less than <ticket>')
def step_impl(context):
    # start bhive
    context.state.ensure_that(context, 'display', '<', 'ticket')
    # end bhive
    context.domain_model.display = 5
    context.domain_model.ticket = 7

@when(u'A customer is called')
def step_impl(context):
    # start bhive
    context.state.assign([('display', ':=', 'display + 1')])
    # end bhive
    context.domain_model.serve_customer()

@when(u'Machine is reset')
def step_impl(context):
    # start bhive
    context.state.assign([('display', ':=', '0')])
    context.state.assign([('ticket', ':=', '1')])
    # end bhive
    context.domain_model.reset()

