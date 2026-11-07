# Reading intake service (synthetic fixture)

The HTTP adapter calls `accept_reading` for POST /readings and `get_reading` for
GET /readings/{id}. The adapter itself is outside this fixture. A queue consumer
calls `process_reading` independently. Storage and queue implementations are injected
interfaces; no cloud, database product, queue product or deployment is specified.

A caller submits an ID, numeric value and unit (C or F). The service stores Accepted,
publishes the ID and returns 202. The queue consumer later converts the value to C
and stores Processed. Unsupported units become Rejected during background handling.
A caller can issue a later GET to retrieve the current stored state. The consumer
does not call a UI or the HTTP adapter when it updates state.

There is no browser interface, message delivery or user approval flow. This fixture
is input for a read-only explanation exercise, not a live service.
