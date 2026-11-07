// Synthetic logical handlers; adapters and UI bindings are outside this fixture.
async function receive(document, store, queue) {
  const request = { ...document, state: 'Received', history: ['Received'] };
  await store.save(request.id, request);
  await queue.publish(request.id);
  return { id: request.id, state: 'Received' };
}

async function scan(id, store) {
  const request = await store.load(id);
  await store.save(id, { ...request, state: 'Ready for review', history: [...request.history, 'Scan complete'] });
}

async function openRequest(id, store) {
  return store.load(id);
}

async function approve(id, revision, reviewer, store) {
  const request = await store.load(id);
  if (request.state !== 'Ready for review' || request.revision !== revision) {
    throw new Error('Retrieve a ready current revision before approval');
  }
  const approved = { ...request, state: 'Approved', reviewer, history: [...request.history, `Approved revision ${revision}`] };
  await store.save(id, approved);
  return approved;
}

module.exports = { receive, scan, openRequest, approve };
