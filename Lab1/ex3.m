function ex3(N,lambda,u)

    arrivals = 1:N;
    departures = 1:N;

    for i = 1:(N)
        u1 = rand;
        arrivals(i) = -(log(1-u1))/lambda;
        u2 = rand;
        departures(i) = -(log(1-u2))/u;
    end
   
    total_arrivals = 1:N;
    total_departures = 1:N;
    
    for i = 1:(N)
        if i==1
            total_arrivals(i) = arrivals(i);
            total_departures(i) = departures(i); 
        else
           total_departures(i) = total_departures(i-1) + departures(i); 
           total_arrivals(i) = total_arrivals(i-1) + arrivals(i);
        end
    end
    
    queue_size_per_time_instant = 1:(ceil(sum(departures)));
    queue_size = 0;
    arrivals_index = 1;
    departures_index = 1;
    total_index = 1;
    limit_events_flag = 0;
    
    
    for i = 1:ceil(max(total_arrivals))
        while (arrivals_index <= N) && (total_arrivals(arrivals_index) <= i)
            if (total_index <= N)
                queue_size = queue_size + 1;
            else
                limit_events_flag = 1;
            end
            arrivals_index = arrivals_index + 1;
            total_index = total_index + 1;
        end
        
        while (departures_index <= N) && (total_departures(departures_index) <= i)
            if (total_index <= N)
                queue_size = queue_size - 1;
            else
                limit_events_flag = 1;
            end
            departures_index = departures_index + 1;
            total_index = total_index + 1;
        end            
        
        if queue_size < 0
            queue_size = 0;
        end
        
        if limit_events_flag == 1
            break;
        
        end
        
        queue_size_per_time_instant(i) = queue_size;
        
    end
    
    queue_size_per_time_instant_final = 1:(i-1);
    
    for i = 1:(i-1)
        queue_size_per_time_instant_final(i) = queue_size_per_time_instant(i);
    end
    
   
    disp('Pratical Average')
    avrg = sum(queue_size_per_time_instant_final)/length(queue_size_per_time_instant_final);
    disp(mean(avrg));
    plot(queue_size_per_time_instant_final);
    disp('Theoretical Average')
    theo_result = lambda/(u-lambda);
    disp(theo_result);
    
end