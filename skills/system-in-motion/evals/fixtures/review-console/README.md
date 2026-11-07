# Review console (synthetic fixture)

This small document-review project has an operator UI, unlike a service-only or CLI
project. The static console.html demonstrates its window, Inbox/Review/History
navigation, request selection, document details and decision table. It is a visual
prototype; the file does not implement bindings or demonstrate a live deployment.

workflow.js defines the logical behavior. A submission is stored Received and a
background scan is enqueued. A separate worker records Ready for review. That write
does not update an operator's screen; openRequest is the explicit retrieval.
A reviewer approves the fetched revision, and that decision becomes request history.

Publishing an approved document is planned only; no publisher exists in the source.
Do not present publication as implemented. Storage, queue, framework and hosting
implementations are unspecified injected interfaces. Do not run the workflow to
explain it or mutate a real document collection.
