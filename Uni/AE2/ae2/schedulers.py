from des import SchedulerDES
import process
import event

class FCFS(SchedulerDES):
    """FCFS Schedualing algorithm - give the process 
    access to the cpu in the order they arrived """
    def scheduler_func(self, cur_event):
     
        for i in self.processes:                                    
            if i.process_state != process.ProcessStates.TERMINATED:
                return i
        
    def dispatcher_func(self, cur_process):
    
        cur_process.process_state = process.ProcessStates.RUNNING       
        cur_process.run_for(cur_process.service_time, self.time)
        cur_process.process_state = process.ProcessStates.TERMINATED
     
        NewEvent = event.Event(process_id=cur_process.process_id , event_type=event.EventTypes.PROC_CPU_DONE ,event_time=(self.time + cur_process.service_time))
        
        return NewEvent

class SJF(FCFS, SchedulerDES):
    """ SJF schedualing algorithm - gives access the process with the 
    shortest rmainging time until being complete access to the cpu first """
    def scheduler_func(self, cur_event):
        
        for i in sorted(self.processes,key = lambda x: x.remaining_time):
            if i.process_state != process.ProcessStates.TERMINATED:         
                if self.time >= i.arrival_time:
                    return i
        
    #Uses dispatcher_func from FCFS because they are the same 
    
class RR(SchedulerDES):
    """RR schedualing algorithm - loops through the avalible process giveing them
    access to the cpu for a set amount of time ot till they complete"""
    def scheduler_func(self, cur_event):
        return self.processes[cur_event.process_id]

    def dispatcher_func(self, cur_process):
        
        timeSpent = min(0.5, cur_process.remaining_time)
       
        cur_process.process_state = process.ProcessStates.RUNNING       
        cur_process.run_for(0.5, self.time)
        
        if cur_process.remaining_time > 0:
            cur_process.process_state = process.ProcessStates.READY      #Not Finished 
            return event.Event(process_id=cur_process.process_id , event_type=event.EventTypes.PROC_CPU_REQ ,event_time=self.time+timeSpent)
           
        elif cur_process.remaining_time == 0:
            cur_process.process_state = process.ProcessStates.TERMINATED #Finsihed 
            return event.Event(process_id=cur_process.process_id , event_type=event.EventTypes.PROC_CPU_DONE ,event_time=self.time+timeSpent)
            
            
class SRTF(SchedulerDES):
    """SRTF schedualing algorithm - looks at the avalible process each time 
    a process arrives of finishes giving access to the cpu to the process 
    with the least remaining time left"""

    def scheduler_func(self, cur_event):
            
        minTime = 10        
        for i in self.processes:
            if i.process_state == process.ProcessStates.READY: 
                if i.remaining_time <= minTime:               
                    minTime = i.remaining_time
                    minProcess = i               
        return minProcess

    def dispatcher_func(self, cur_process):
        
        timeSpent = min(self.next_event_time() - self.time, cur_process.remaining_time)
       
        cur_process.process_state = process.ProcessStates.RUNNING       
        cur_process.run_for(self.next_event_time() - self.time, self.time)
        
        if cur_process.remaining_time > 0:
            cur_process.process_state = process.ProcessStates.READY      #Not Finished 
            return event.Event(process_id=cur_process.process_id , event_type=event.EventTypes.PROC_CPU_REQ ,event_time=self.time+timeSpent)
            
        elif cur_process.remaining_time == 0:
            cur_process.process_state = process.ProcessStates.TERMINATED #Finsihed 
            return event.Event(process_id=cur_process.process_id , event_type=event.EventTypes.PROC_CPU_DONE ,event_time=self.time+timeSpent)
            