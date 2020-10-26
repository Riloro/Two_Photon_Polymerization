%{
    
    Plane equation and 3D translation | 2photon_polimerization
    -> Ricardo Lopez Rodriguez 
  --------------------------------------------------------------------------------------------------------
    This code is a simulation of how the imaginary plane of the sample
    is going to be translated along a coordinate system ....
    
    Plane equation --->
    Ax + By + Cz = D;

    3D linear transformation ???---->
    |Phi'> = T |Phih>
%}


function twoPhotonPolySimulation()

    clear all; 
    close all;
    set(0,'defaultTextInterpreter','latex');   
    
    move = true;
    up = true;
    animation = false;
    view90 = false;
    N = 50; % Number of points for ploting
    mesuredPoints = [50,30,4.5;35,80,3;-90,45,3]; % Mesured points by fluorescence
    V1 = zeros(1,3); % Vector V1
    V2 = zeros(1,3); % Vector V2
    
    %----------------Calculating the normal vector components---------------
    
     

    for i = 1 : length(mesuredPoints)  
        
        V1(i) = mesuredPoints(2,i) - mesuredPoints(1,i);   %Computing the vector components of V1 and V2
        V2(i) = mesuredPoints(3, i) - mesuredPoints(1,i);

    end      
    
    normalV = cross(V2,V1); % Normal vector    
    normalVector = normalV./norm(normalV) ; %Normalized normal vector
    
    disp("NormalVector =");
    disp(normalVector);
    
    n_x = normalVector(1);
    n_y = normalVector(2);
    n_z = normalVector(3);
    
    %----------------Therefore we can generate the plane equation   nx X + ny Y + nz Z = D as, --------------
  
    D = dot(normalVector, mesuredPoints(1,:));
    disp(mesuredPoints(1,:));
    
    
    % xrage 200 micron   yrange 200 micron   z 20 micron ---- > 
    % x e[-100,100] ;y e[-100,100] ;z [-10, 10]  PiezoStage Range in microns
    
    points = linspace(-100,100,N);
    [X,Y] = meshgrid(points);
    Z = ( D - ( n_x .* X + n_y .*Y ) )./(n_z) ;   % PLANE EQUATION
    
    f = figure;
   
    
    ZPiezo = zeros(N,N); %Piezo stage plane
    surf(X,Y,ZPiezo);
    
    colormap(f,winter);
    hold on
    grid on
    if view90 == true
        view(90,0);
    end
    xlabel('X $(\mu m)$');
    ylabel('Y $(\mu m)$');
    zlabel('Z $(\mu m)$');
    title("Piezo stage Position and Imaginary Plane")
    xlim([-120,120]);
    ylim([-120,120]);
    zlim([-20,20]);
    
    
    surf(X,Y,Z);
   
    
    for i = 1 : 3      
       plot3(mesuredPoints(i,1),mesuredPoints(i,2),mesuredPoints(i,3),'o','Color','r','MarkerSize',5,'MarkerFaceColor','r');        
    end
   
    plot3(0,0,10,'*','Color',[1 0 1],'MarkerSize',10,'MarkerFaceColor','b');
    
    
    
    if move == true 
        % ..............................Writing on the plane...................
   
        P = [40, 50,0];
        plot3(P(1),P(2),P(3),'o','Color',[1 0 1],'MarkerSize',5,'MarkerFaceColor',[1 0 1]);

        zUp = ( D - ( n_x .* P(1) + n_y .* P(2) ) )./(n_z) ; 
        Pup = [40,50,zUp,1];                                % Point on the imaginary plane    
        plot3(Pup(1),Pup(2),Pup(3),'o','Color',[1 0 1],'MarkerSize',5,'MarkerFaceColor',[1 0 1]); % Ploting the point of interest

        % ..............................Linear Translation................
        % ..............................|Phi'> = T |Phi>................

        phi = ones(4,1);
        phiPrime = ones(4,length(X));

        t_z = 0;
        t_x = -Pup(1);
        t_y = -Pup(2);
        T = [1,0,0,t_x;0,1,0,t_y;0,0,1,t_z;0,0,0,1]; % Transformation Matrix T....
        Ptras = T * transpose(Pup);
        plot3(Ptras(1,1),Ptras(2,1),Ptras(3,1),'o','Color',[1 0 1],'MarkerSize',5,'MarkerFaceColor',[1 0 1]); %Ploting update after translation
        pause on    
        counter = 1;
        for i = 1 : length(X)
            for j = 1 : length(X)  
                
                phi(1,1) = X(j,i);
                phi(2,1) = Y(j,i);
                phi(3,1) = Z(j,i);
                
                phiPrime(:,counter) = T * phi;   % Translated Points  phiPrime.....
            
                xPrime = phiPrime(1,counter);
                yPrime = phiPrime(2,counter);
                zPrime = phiPrime(3,counter);
              
                plot3(xPrime,yPrime,zPrime,'o','Color','g','MarkerSize',2,'MarkerFaceColor','g');           
                plot3(xPrime,yPrime,0,'o','Color','r','MarkerSize',2,'MarkerFaceColor','r');
                
                counter = counter + 1;
                if animation == true
                    pause(.00001);
                end
            end    
        end
        P = [40, 50,0,1];
        Pnew = T * transpose(P);
        plot3(Pnew(1,1),Pnew(2,1),Pnew(3,1),'o','Color',[1 0 1],'MarkerSize',5,'MarkerFaceColor',[1 0 1])
       
        if up == true    
            sz = size(phiPrime); % N*N puntos
            
            t_z = 10 - Pup(3);  % Z translation is given by the subtraction between the "Tip" z position and zP
            t_x = 0;
            t_y = 0;
            T_2 = [1,0,0,t_x;0,1,0,t_y;0,0,1,t_z;0,0,0,1]; % Transformation Matrix T....
            
            PtrasNew = T_2 * Ptras;
            phiPrime2 = ones(4,length(X));
            z_0 = 0;
            
            for j = 1 : sz(2)
                
                phiPrime2(:,j) = T_2 * phiPrime(:,j); %Linear transformation
                
                xPrime2 = phiPrime2(1,j);
                yPrime2 = phiPrime2(2,j);
                zPrime2 = phiPrime2(3,j);                
                plot3(xPrime2,yPrime2,zPrime2,'o','Color','g','MarkerSize',2,'MarkerFaceColor','g');           
                plot3(xPrime2,yPrime2,z_0 + t_z,'o','Color','r','MarkerSize',2,'MarkerFaceColor','r') 
            end              
            %Ploting update after z translation          
            plot3(PtrasNew(1,1),PtrasNew(2,1),PtrasNew(3,1),'o','Color',[1 0 1],'MarkerSize',5,'MarkerFaceColor',[1 0 1]); 
        end
    end   
    
end