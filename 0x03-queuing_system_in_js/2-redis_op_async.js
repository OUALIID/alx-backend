import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const displaySchoolValue = async schoolName => console.log(await getAsync(schoolName));
const setSchool = async (schoolName, value) => await setAsync(schoolName, value);

(async () => {
  await displaySchoolValue('Holberton');
  await setSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
