# M-M-1-Queue-Simulation
This program simulates an M/M/1 Queue in Python

# M/M/1 Queue
Much of this is motivated from https://en.wikipedia.org/wiki/M/M/1_queue.

The state space is the set {0,1,2,3,...}, where the value corresponds to the number of customers in the system. 
We let Pn denote the probability of n customers in the system.

Arrivals occur at rate λ according to a Poisson process, which moves the system from state i to state i+1 (since 
a customer as arrived). Service times are exponentially distributed with rate parameter μ so that 1/μ is the mean service time.

A single server serves customers one at a time from the front of the queue, according to a first-come, first-served discipline. When the service is complete the customer leaves the queue and the number of customers in the system reduces by one, i.e., the system moves from state i to i−1.

Suppose the system is in state n. Then, the balance equation reads

(λ+μ)Pn = λPn−1 + μPn+1

Essentially,
(λ+μ)Pn:  rate of an arrival or departure to Pn
λPn−1:    rate of an arrival to Pn−1
μPn+1:    rate of a departure from Pn+1

The boundary condition (near an empty queue) is that
λP0=μP1.

Thus,
P1 = λ/μ(P0)

P2 = λ/μ(P1) + 1/μ(μP1−λP0 )= λ/μ(P1) = (λ/μ)^2(P0)

Pn =(λ/μ)^n(P0)
