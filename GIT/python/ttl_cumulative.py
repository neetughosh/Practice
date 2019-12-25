requests = [ {'requestId': 'poiax',  'startedAt': 1489744808, 'ttl': 8},
			 {'requestId': 'kdfhd',  'startedAt': 1489744803, 'ttl': 3},
			 {'requestId': 'uqwyet', 'startedAt': 1489744806, 'ttl': 12},
			 {'requestId': 'qewaz',  'startedAt': 1489744810, 'ttl': 1} ]

cumulativeTtl = 15

# fetch the startedAt and ttl values
(startedAt_list, ttl) = zip(*[(x['startedAt'], x['ttl']) for x in requests])

# Extract the minimum of startedAt
minimum = min(startedAt_list)

# Extract the maximum of startedAt and ttl and add them
maximum = max(startedAt_list) + max(ttl)
    
# difference of minimum startedAt and (maximum of startedAt + maximum of ttl is the cumulative ttl)
cummulativeTtl = (maximum - minimum)

print(cumulativeTtl)

#print((result == cumulativeTtl) ? True : False)


#var max = result = 0;
#var min = requests[0].startedAt;
#


#requests.forEach(request => {
#  const completeAt = request.startedAt + request.ttl;
#  if (request.startedAt < min) {
#    min = request.startedAt;
#  }
#  if (completeAt > max) {
#    max = completeAt;
#  }
#});
#
#var cummulativeTtl = (max - min);
#
#console.log(cumulativeTtl)
#
#console.log((result == cumulativeTtl) ? true : false);
