# G1. Systems Architecture
## Prompt to give the system under test
You are advising a startup with two engineers and three weeks before a nationally
televised product launch.
Current architecture:
- One PostgreSQL database stores users, products, inventory, and orders.
- A Node.js monolith serves all API requests.
- Redis caches inventory counts with a 60-second TTL.
- Checkout performs a synchronous payment authorization through Stripe before
completing the order.
- A nightly reconciliation process compares orders against inventory and corrects
discrepancies.
Traffic is expected to increase by approximately 200 times for several hours after
launch.
Analyze this architecture.
Specifically:
1. What component is most likely to fail first?
2. What failure would have the greatest business impact?
3. What architectural changes would you implement within the available three weeks?
4. What improvements would you deliberately postpone until after launch?
5. Identify any assumptions in the scenario that could change your recommendations.
Explain your reasoning rather than simply listing recommendations.
