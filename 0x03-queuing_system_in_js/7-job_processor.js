const kue = require('kue');

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    if (blacklistedNumbers.includes(phoneNumber)) {
        console.log(`Notification job ${job.id} failed: Phone number ${phoneNumber} is blacklisted`);
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

const queue = kue.createQueue();

queue.process('push_notification_code_2', (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});
