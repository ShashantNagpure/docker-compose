from tasks.enums import TaskPriority, TaskStatus

    
post_create_priority_to_status_transitions_map = {
    
    # task priority: (task status, delay in seconds)
    TaskPriority.HIGH : [(TaskStatus.STATUS_1, 30),(TaskStatus.STATUS_2, 60)],
    TaskPriority.LOW : [(TaskStatus.STATUS_1, 60),(TaskStatus.STATUS_2, 120)],
    TaskPriority.LOWEST : [(TaskStatus.STATUS_1, 120),(TaskStatus.STATUS_2, 300)]
}
