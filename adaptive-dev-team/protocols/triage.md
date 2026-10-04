# Triage Engine

## Task Triage Results

### TRIAGE RESULT
Task Type: [Bug Fix | Small Change | Feature | Large Feature | Greenfield | Refactor | Migration | Optimization | Research + Implementation | Release]
Complexity: [Trivial | Small | Medium | Large | Critical]
Risk: [Low | Medium | High | Critical]
Uncertainty: [Low | Medium | High]
Blast Radius: [Local | Module | Multi-module | System-wide]
Domains: [Frontend | Backend | Database | Mobile | Desktop | Game | AI/ML | 3D | Infrastructure | Other | Mixed (multiple selections)]
Parallel Potential: [None | Low | Medium | High]
Workflow: [Selected workflow based on triage]
Required Roles: [...]
Optional Roles: [...]
Skipped Roles: [...]
Reason: [...]

## Core Triage Principles

### Minimum Sufficient Team
- Start with only essential roles for the task type and complexity
- Add optional roles only when expertise gaps are confirmed
- Skip roles when task falls within core team capabilities

### Dynamic Composition
- Adjust team size based on task complexity and risk
- Maintain lean teams for small changes (1-2 people)
- Scale up for large features and research-heavy tasks
- Include specialized roles only when specific expertise is needed

### Evidence Before Completion
- Validate requirements before work begins
- Confirm scope boundaries before task assignment
- Verify dependencies before task execution

## Decision Matrix

| Task Type | Default Complexity | Risk Level | Parallel Potential |
|-----------|-------------------|------------|-------------------|
| Bug Fix | Trivial | Low | Low |
| Small Change | Small | Low | None |
| Feature | Medium | Medium | Low |
| Large Feature | Large | High | Medium |
| Greenfield | Large | Critical | Medium |
| Refactor | Medium | Medium | Medium |
| Migration | Large | High | Medium |
| Optimization | Small | Low | Medium |
| Research + Implementation | Critical | High | High |
| Release | Large | Medium | Low |

## Domain Classification

### Frontend
- UI components
- User interactions
- Frontend optimization
- Client-side logic

### Backend  
- API development
- Server-side logic
- Database operations
- Infrastructure concerns

### Database
- Schema changes
- Data migrations
- Performance tuning
- Data integrity

### Mobile
- Native features
- Platform-specific logic
- Cross-platform issues
- Mobile-specific bugs

### Desktop
- Desktop-specific features
- System integration
- Local storage
- Native UI components

### Game
- Gameplay mechanics
- Game logic
- Performance optimization
- Asset management

### AI/ML
- Model training
- Data processing
- Algorithm implementation
- Experimentation

### 3D
- 3D modeling
- Graphics rendering
- Physics simulation
- 3D interactions

### Infrastructure
- Deployment
- Monitoring
- Scaling
- Security

### Other
- Documentation
- Process improvement
- Training
- Planning

### Mixed
- Cross-domain tasks
- Integration projects
- Multi-component changes