module.exports = {
  API_BASE: 'http://localhost:8000/',

  ENTRYPOINTS: {
    HOME: process.env.HOME_PATH || 'home',
    EVENTS: process.env.EVENTS_PATH || 'events',
    PROJECTS: process.env.PROJECTS_PATH || 'projects',    
  }
};
