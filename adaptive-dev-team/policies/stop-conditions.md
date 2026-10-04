# Stop Conditions Policy

## Core Principle: Stop When Further Work is Unnecessary

Stop spawning agents when the conditions below are met. This prevents unnecessary work and resource waste.

## When to Stop

### New Agent Has No Independent Ownership
- The task can be handled by existing agents
- No unique expertise needed
- Ownership is not clearly assigned
- The role would exist only to satisfy a process diagram

### New Agent Duplicates Existing Roles
- Overlap in capabilities
- Redundant functionality
- No distinct value proposition
- A Builder Lead with only one Builder to coordinate, or a Specialist whose trigger did not fire

### Parallelism Has Reached Dependency Limits
- All tasks are now sequential
- No remaining independent work
- Blocked by dependencies

### Task is Sufficiently Simple
- Can be completed within reasonable time
- Does not require multiple skill sets
- Can be handled by one agent

### Spawn Overhead > Expected Benefit
- Time to spawn exceeds work value
- Cost of spawning exceeds benefit
- Resources are better used elsewhere

### All Remaining Tasks Strongly Depend on Current Work
- Other tasks are blocked on current work
- No parallel work can proceed
- Dependencies cannot be resolved earlier

### Agent Budget Has Clearly Become Unreasonable
- Agents are not contributing
- Budget is excessive for the task
- Better alternatives exist

## When to Continue

Only continue when the above conditions are not met:
- Work requires diverse expertise
- Multiple independent tasks exist
- Parallel work is possible
- Benefits justify overhead
- Dependencies are resolved

## Dynamic Evaluation

### Continuous Monitoring
- Regularly review agent productivity
- Track task completion rates
- Monitor resource utilization
- Check for diminishing returns

### Evidence-Based Decisions
- Make decisions based on data, not opinion
- Look at completion rates and quality
- Consider time and resource costs
- Evaluate opportunity costs

## Escalation

When conditions are ambiguous:
- Consult with leadership
- Review task criticality
- Evaluate resource constraints
- Consider alternative approaches

## Skipping Absent Optional Roles

When a workflow names a role that is not active (no Builder Lead, no Specialist, no Integration Engineer):

- Skip that stage and route to the nearest active authority; a Builder → Leader path is valid.
- Never spawn an optional role merely to keep the process shape intact.
- Record the skip in one line so the skipped stage is not mistaken for a passed gate.

## Review Points

### Daily Check
- Are tasks still active?
- Are agents productive?
- Can work be parallelized?

### Weekly Check
- Have conditions changed?
- Are we overstaffed?
- Is the budget reasonable?

## Special Cases

### Complex Tasks
- May require more agents than expected
- May require deeper investigation
- May need more time to evaluate

### Critical Path Tasks
- Cannot be stopped mid-execution
- Must complete critical dependencies
- May require additional resources

### Emergency Situations
- May require temporary overstaffing
- May need additional agents
- May require different composition