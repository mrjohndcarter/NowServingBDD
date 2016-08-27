from behave import given, when, then

from Implementation import NowServing


@given(u'Machine is off')
def step_impl(context):
    # bhive assert : status == off
    # bhive needs to know about type off
    context.machine.status = NowServing.NowServing.Status.off


@when(u'Machine is started')
def step_impl(context):
    # bhive needs to know what?  is this just the name of a state change?
    context.machine.start()


@then(u'The next ticket should be 1')
def step_impl(context):
    # bhive needs to know what?  this is an assertion of the machine state
    assert context.machine.take_ticket() == 1


@then(u'The "Now Serving" display should be blank')
def step_impl(context):
    assert context.machine.display == ''

@given(u'Machine is on')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Machine is on')


@when(u'A ticket is dispensed')
def step_impl(context):
    raise NotImplementedError(u'STEP: When A ticket is dispensed')


@then(u'The ticket should be less than the displayed number')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The ticket should be less than the displayed number')


@given(u'Wicket <wicket> is open')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Wicket <wicket> is open')


@when(u'Wicket <wicket> serves a customer with ticket <ticket>')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Wicket <wicket> serves a customer with ticket <ticket>')


@then(u'The "Now Serving" display should show <wicket> is serving <ticket>')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The "Now Serving" display should show <wicket> is serving <ticket>')


@when(u'Wicket <wicket> is closed')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Wicket <wicket> is closed')


@then(u'The "Now Serving" display should now show <wicket>')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The "Now Serving" display should now show <wicket>')


@when(u'Machine is stopped')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Machine is stopped')


@then(u'Machine is off')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Machine is off')
