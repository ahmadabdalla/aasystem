# Parcel project fixture

Materialize these files at their project-relative paths. The source is intentionally small. No runtime has been exercised for this fixture.

## `src/invoice.js`

```js
let latestInvoice = null;

export function applyInvoice(a, channel) {
  const x = { recipient: a.email, cents: a.amount };

  if (a.retry) {
    channel.send(x);
    latestInvoice = a.id;
  } else if (a.dryRun) {
    latestInvoice = a.id;
  } else {
    channel.send(x);
    latestInvoice = a.id;
  }

  return latestInvoice;
}

export function retryInvoice(a, channel) {
  if (latestInvoice === a.id) {
    return applyInvoice({ ...a, retry: true }, channel);
  }

  return null;
}
```

## `src/run-invoice.js`

```js
import { applyInvoice, retryInvoice } from "./invoice.js";

export function runInvoice(input, channel) {
  const id = applyInvoice(input, channel);
  return input.retryLater ? retryInvoice({ ...input, id }, channel) : id;
}
```

## `src/delivery.js`

```js
export const deliveries = new Map();

export function submitDelivery(form, legacyQueue) {
  const delivery = {
    id: form.id,
    destination: form.address,
    message: form.note,
    state: "queued"
  };
  deliveries.set(delivery.id, delivery);
  legacyQueue.write(toLegacyQueueMessage(delivery));
  return delivery;
}

export function markDelivered(id) {
  deliveries.get(id).state = "delivered";
}

export function toLegacyQueueMessage(delivery) {
  return { dest: delivery.destination, text: delivery.message, trace: delivery.id };
}
```

## `src/run-delivery.js`

```js
import { submitDelivery } from "./delivery.js";

export function runDelivery(form, legacyQueue) {
  const delivery = submitDelivery(form, legacyQueue);
  delivery.state = "sent";
  return delivery.id;
}
```

## `src/receipt.js`

```js
export function receiptLabel(receipt) {
  return `${receipt.id}: ${receipt.totalCents} cents`;
}
```

## `docs/legacy-queue-contract.md`

```md
# Legacy queue contract

The vendor queue accepts only `{ dest, text, trace }`. Keep the translation from the application's delivery record at the integration boundary so application callers do not construct vendor messages. The queue migration is not authorized by this exercise.
```

## `records/settled-refactoring-target.md`

```md
# Settled local target

An earlier assessment selected instance-local invoice attempt state and an explicit delivery transition owned by the delivery module. Preserve the legacy queue translation boundary, public caller compatibility until migration is planned, and existing delivery semantics. The next phase is a local structural reshape followed by public-surface equivalence checks. Do not repeat the assessment unless the source or constraints change materially.
```
