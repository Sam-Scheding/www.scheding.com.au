import { explode } from 'cron-bomb';
import { API_BASE } from '../../constants';
import axios from 'axios';

export default {
  async getEvents(start, end) {

    const url = `${API_BASE}events/json`;
    const data = await axios({
      method: 'get',
      url,
    }).then(response => response.data);
    const debris = explode({start, end, data});
    return debris;
  },
  async postEvent(start, end) {

    const url = `${API_BASE}events/json`;
    const data = await axios({
      method: 'post',
      url,
    }).then(response => response.data);
    const debris = explode({start, end, data, utc:true});

    console.log(debris);
    return debris;
  },

}
