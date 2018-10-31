function lambdat = ex23(n,lambda1,lambda2,lambda3)
    lambdat = zeros(3,n);
    j = 1;
    lambdas = [lambda1,lambda2,lambda3];
    time=n/max(lambdas);
    limit(1)= ceil(lambda1*time);
    limit(2)= ceil(lambda2*time);
    limit(3)= ceil(lambda3*time);
    while j <= 3
        i = 1;
        while i <= limit(j)
            if  i==1
                number1 = rand;
                lambdat(j,i) = - log (1 - number1) / lambdas(j);
            else
                number2 = rand;
                lambdat(j,i) = lambdat(j,i-1) + (- log (1 - number2) / lambdas(j));
            end
            i = i + 1;
            
        end
        j = j + 1;
    end
    
    lambdat=sort(lambdat(lambdat>0));
    nrocorrencias = 1:ceil(lambdat(length(lambdat)));
    nrocorrencias = zeros(1, ceil(lambdat(length(lambdat))));
    ii = 1;
    while ii <= length(lambdat)
        index=ceil(lambdat(ii));
        nrocorrencias(index)=nrocorrencias(index)+1;
        ii = ii + 1;
    end
    pratical = probability(nrocorrencias); 
    zeross = 0:max(nrocorrencias);
    bar(zeross,pratical)
    ylabel('Probability')
    xlabel('#Events on a unitary period')
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
        
        
        
   

