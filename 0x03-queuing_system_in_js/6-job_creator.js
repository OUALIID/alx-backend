const queue = require('kue').createQueue();

const jobData = {
  phoneNumber: '0001010100',
  message: 'I feel so sad',
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
