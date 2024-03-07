function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach(job => {
        const jobInstance = queue.create('push_notification_code_3', job).save();
        
        console.log(`Notification job created: ${jobInstance.id}`);

        jobInstance.on('complete', () => {
            console.log(`Notification job ${jobInstance.id} completed`);
        });

        jobInstance.on('failed', (err) => {
            console.error(`Notification job ${jobInstance.id} failed: ${err}`);
        });

        jobInstance.on('progress', (progress) => {
            console.log(`Notification job ${jobInstance.id} ${progress}% complete`);
        });
    });
}

export default createPushNotificationsJobs;
