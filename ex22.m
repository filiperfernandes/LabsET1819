function lambdat = ex22(n,lambda)
    i = 1;
    lambdat = 1:n;
    while i <= n
        if i == 1
            number = rand;
            lambdat(i) = - log (1 - number) / lambda;
        else
            number = rand;
            lambdat(i) = lambdat(i-1) + (- log (1 - number) / lambda);
        
        end
        i = i + 1;
        
    end
    
    nrocorrencias = 1:ceil(lambdat(n));
    nrocorrencias = zeros(1, ceil(lambdat(n)));
    ii = 1;
    while ii <= n
        index=ceil(lambdat(ii));
        nrocorrencias(index)=nrocorrencias(index)+1;
        ii = ii + 1;
    end
    zerosss = 0:ceil(lambdat(length(lambdat)))-1;
    figure
    bar(zerosss,nrocorrencias)
    ylabel('#Events')
    xlabel('Time Interval')
    
    
    pratical = probability(nrocorrencias); 
    
    theoretical= 1:length(pratical);
    iii = 1;
    while iii <= length(theoretical)
        theoretical(iii)= poissonarrival(iii-1,lambda);
        iii = iii + 1;
        
    end
    
    zeross = 0:max(nrocorrencias);
    figure
    w1=0.5;
    bar(zeross,pratical,w1)
    w2=0.25;
    hold on
    bar(zeross,theoretical,w2)
    hold off
    grid on
    ylabel('Probability')
    xlabel('#Events on a unitary period')
    legend({'Practical','Theoretical'},'Location','northeast')
    
end



function result = poissonarrival(k,lambda)

result = lambda^k / factorial(k)* exp(-lambda);

end


function probabilities = probability(array)
    probabilities= 1:max(array)+1;
    count=0;
    i = 0;
    while i <= max(array)
        j = 1;
        while j <= length(array)
            if i==array(j)
                count = count + 1;
            end
            j = j + 1;
        end
        

        probabilities(i+1)=count/length(array);
        count=0;
        i = i + 1;
    end
    
end
    