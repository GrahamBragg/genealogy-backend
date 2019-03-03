const express = require('express');

const { errorHandler } = require('../middleware');

// list of models here
const { Question } = require('../models/question');
const { Event } = require('../models/event')

// list of controllers here
const questions = require('../controllers/questions');
const events = require('../controllers/events');

// combine models ino one object
const models = { Question, Event };

const routersInit = config => {
  const router = express();

  // register api points
  router.use('/questions', questions(models, { config }));
  router.use('/events', events(models, { config }));

  // catch api all errors
  router.use(errorHandler);
  return router;
};

module.exports = routersInit;