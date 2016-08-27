@given(u'Machine is off')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Machine is off')


@when(u'Machine is started')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Machine is started')


@then(u'The next ticket should be 1')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The next ticket should be 1')


@then(u'The "Now Serving" display should be blank')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The "Now Serving" display should be blank')


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
