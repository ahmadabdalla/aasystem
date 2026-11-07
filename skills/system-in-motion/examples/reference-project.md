# Synthetic equipment service request

This fictional reference demonstrates the explanation pattern. It describes no
customer, repository, cloud deployment or live integration. The implementation
names are roles rather than vendor recommendations.

## Request intake

A visitor submits an equipment request in the web application. An HTTP service
validates it, stores a pending request and publishes an availability-check task.
The page displays Pending; receiving the task does not initiate a browser request.

## Background availability

A separate consumer receives the queued task. It reads inventory through an adapter
and persists the availability result in the relational request store. No browser
or HTTP-service call is required to perform this background write.

## Human review

A coordinator later opens the operations view. That deliberate action initiates
an HTTP request and reads the stored result. The coordinator reviews the available
equipment and approves the request. The same HTTP service records the approval.

## Planned notification

Notification is a future addition in this reference. The HTTP service would submit
an approved confirmation to a messaging provider and record Pending delivery.
A later provider event would reach the HTTP service, which would record delivery
evidence. Submission alone would not establish that delivery succeeded.

## Included and omitted

Included: actors, input, background handoff, result visibility, explicit review,
approval, pending delivery and planned evidence. Omitted: hosting, authentication,
pricing, infrastructure operations, error recovery and production reliability.
The reference is intentionally a bounded journey rather than a complete system.
