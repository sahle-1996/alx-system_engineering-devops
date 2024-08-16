Issue Summary

Duration of the Outage:
Start: August 15, 2024, 17:00 EAT
End: August 15, 2024, 19:30 EAT
Total Duration: 2 hours 30 minutes



Impact:
During the outage, our main website became completely inaccessible, leaving approximately 75% of our users staring at 404 error pages. This disruption severely impacted our online sales and user engagement during peak hours, as customers couldn't place orders or access their accounts.


Root Cause:
The root cause was traced back to a simple yet catastrophic misconfiguration in the Nginx server during a routine update. A single incorrect setting prevented the server from properly routing incoming requests, effectively cutting off access to our services.


Timeline


17:00 EAT: Our monitoring system detected a sharp drop in web traffic and immediately fired off alerts to the team.
17:05 EAT: A dedicated engineer on call received the alert via Slack and jumped into action.
17:15 EAT: The initial hypothesis pointed fingers at a recent deployment, leading to a rollback attempt. Unfortunately, this did not fix the issue.
17:25 EAT: Further investigations commenced, focusing on server logs, but these led to a false trail, with suspicions falling on a possible database connectivity issue.
17:45 EAT: Realizing the dead-end, the incident was escalated to the DevOps team for deeper analysis.
18:00 EAT: After a thorough review, the DevOps team discovered the misconfiguration in the Nginx server.
18:15 EAT: The offending configuration was corrected, and the Nginx server was restarted.
18:30 EAT: Service was restored, and customers could once again access the website.
19:30 EAT: Post-resolution monitoring confirmed that the site was stable and operating normally.






Root Cause and Resolution



Root Cause:

During a routine server update, an incorrect directive was inadvertently added to the Nginx configuration file. This misconfiguration caused the server to mishandle incoming requests, leading to the complete inaccessibility of our website. The issue was not caught earlier because the test environment didn't fully mirror the production setup, which allowed the error to slip through.


Resolution:

After identifying the faulty configuration, the team quickly corrected the directive. The Nginx server was then restarted, which successfully restored access to the website. To ensure the issue was fully resolved, extensive post-restart testing was conducted, confirming that all services were back online and functioning correctly.


Corrective and Preventative Measures

Improvements:

Upgrade the testing environment to more accurately replicate production conditions, including server configurations.
Implement a detailed pre-deployment checklist that includes reviewing critical server configuration files.
Enhance monitoring systems to include checks for common misconfigurations, especially in critical services like Nginx.


Tasks:

 Update the Nginx server with more robust error-checking mechanisms to catch configuration mistakes before deployment.
 Develop specific alerts for Nginx configuration issues, ensuring quicker detection.
 Organize a training session for the engineering team focusing on best practices in server management and configuration.
 Implement an automated rollback process that includes resetting configuration files to their last known good state.



