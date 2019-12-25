requests = [ {requestId: 'poiax',  startedAt: 1489744808, ttl: 8},
			 {requestId: 'kdfhd',  startedAt: 1489744803, ttl: 3},
			 {requestId: 'uqwyet', startedAt: 1489744806, ttl: 12},
			 {requestId: 'qewaz',  startedAt: 1489744810, ttl: 1} ]

cumulativeTtl = 15

var max = result = 0;
var min = requests[0].startedAt;

requests.forEach(request => {
  const completeAt = request.startedAt + request.ttl;
  if (request.startedAt < min) {
    min = request.startedAt;
  }
  if (completeAt > max) {
    max = completeAt;
  }
});

const cummulativeTtl = (max - min);

console.log(cumulativeTtl)

console.log((result == cumulativeTtl) ? true : false);