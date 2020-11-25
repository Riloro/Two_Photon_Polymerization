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
    N = 40; % Number of points for ploting
    mesuredPoints = [50,30,4.5;35,80,3;-90,45,3]; % Mesured points by fluorescence
    V1 = zeros(1,3); % Vector V1
    V2 = zeros(1,3); % Vector V2
    
    
    %---------------------------Polygon-----------------------------%
    ref_point = [5,0,0];
    n_sides = 3;
    R = 2 ;
    res = 0.1;
   % polygon(n_sides,R, ref_point, res); 
    %.......................................Writing a 3D line.................................................%
    r_0 = [1,0,0];
    r = [90,50,5];
    resolution = 4; % um      resolution
    %lineConstruction(r_0,r,resolution,6)
    hold on
    r_0 = [1,0,0];
    r = [90,50,-5];
    %lineConstruction(r_0,r,resolution,6)
    
    % ......................Building a cube................................
    v1 = [-50,50,0];
    v2 = [50,50,0];
    v3 = [-50,-50,0];
    v4 = [50,-50,0];
    deltaX = resolution;
    h = 20;
    %cube(v1,v2,v3,v4,deltaX,resolution,h)
    %----------------Calculating the normal vector components---------------............   
     

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
    disp("Mesured Points:")
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
    title("Piezo stage and substrate-sample plane")
    xlim([-120,120]);
    ylim([-120,120]);
    zlim([-20,20]);
    
    
    surf(X,Y,Z);
   
    
    for i = 1 : 3      
       plot3(mesuredPoints(i,1),mesuredPoints(i,2),mesuredPoints(i,3),'o','Color','r','MarkerSize',5,'MarkerFaceColor','r');        
    end
   
    plot3(0,0,10,'*','Color',[1 0 1],'MarkerSize',10,'MarkerFaceColor','b');   % Focal Objective´s point
    
    
    
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
      %  T = [1,0,0,t_x;0,1,0,t_y;0,0,1,t_z;0,0,0,1]; % Transformation Matrix T....
        
        Ptras = translation(t_x,t_y,t_z,Pup); %T * transpose(Pup);
        plot3(Ptras(1,1),Ptras(2,1),Ptras(3,1),'o','Color',[1 0 1],'MarkerSize',5,'MarkerFaceColor',[1 0 1]); %Ploting update after translation
        pause on    
        counter = 1;
        
        for i = 1 : length(X)
            for j = 1 : length(X)  
                
                phi(1,1) = X(j,i);
                phi(2,1) = Y(j,i);
                phi(3,1) = Z(j,i);
                
                phiPrime(:,counter) = translation(t_x,t_y,t_z,phi);  %T * phi;   % Translated Points  phiPrime.....
            
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
        Pnew = translation(t_x,t_y,t_z,transpose(P)); %T * transpose(P);
        plot3(Pnew(1,1),Pnew(2,1),Pnew(3,1),'o','Color',[1 0 1],'MarkerSize',5,'MarkerFaceColor',[1 0 1])
       
        if up == true    
            sz = size(phiPrime); % N*N points
            
            t_z = 10 - Pup(3);  % Z translation is given by the subtraction between the "Objective's focal point" z position and zP
            t_x = 0;
            t_y = 0;
            %T_2 = [1,0,0,t_x;0,1,0,t_y;0,0,1,t_z;0,0,0,1]; % Transformation Matrix T....
            
            PtrasNew = translation(t_x,t_y,t_z,Ptras); %T_2 * Ptras;
            phiPrime2 = ones(4,length(X));
            z_0 = 0;
            
            for j = 1 : sz(2)
                
                phiPrime2(:,j) = translation(t_x,t_y,t_z,phiPrime(:,j)); %T_2 * phiPrime(:,j); %Linear transformation
                
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





function vertices = polygon(n_sides,R, ref_point, resolution)
    
    
    z = 0;
    N = 1;  % Number of planes 

    % Writing the Polygon on the N planes
    for m = 1 : N
        coordinates = zeros(n_sides,2);
        position = zeros(1,3);  
        for i = 1 : n_sides 
            
            phi = (i - 1) * (2*pi/n_sides) ;                % Computing the vertices position 
            position(i,1) = ref_point(1) + R*cos(phi);
            position(i,2) = ref_point(2) + R*sin(phi);      
            position(i,3) = z;

        end


        for k = 1 : n_sides

            figure(3)
            plot3(position(k,1),position(k,2),position(k,3),'-o','Color',[1 0 1],'MarkerSize',...
                5,'MarkerFaceColor','b');
            xlabel("X")
            ylabel("Y")
            zlabel("Z")
            title("Printing Polygons")
            grid on
            hold on



    %         figure(4)
    %         plot(position(k,1),position(k,2),'o','Color',[1 0 1],'MarkerSize',...
    %             5,'MarkerFaceColor',[1 0 1]);
    %         
    %         grid on
    %         hold on
    %         
        end
        z = m*resolution ;
    end
    
    vertices = position;
    U = zeros(1,3);
    
    for i = 1 : n_sides
        
       if (i + 1) > n_sides
           U(1) =  position(1, 1) - position(i,1);
           U(2) =  position(1, 2) - position(i,2);
           U(3) =  position(1, 3) - position(i,3);           
       else
           U(1) =  position(i + 1, 1) - position(i,1);
           U(2) =  position(i + 1, 2) - position(i,2);
           U(3) =  position(i + 1, 3) - position(i,3);
       end
       
       
       mag(i) = norm(U);
       
       %unitary vecto u ...
       disp("u = ")
       u = U./norm(U) ;
       disp(u);
       unitaryVectors(i,:) = u ;    
            
        
    end
    
    magnitude = false;
    i = 1;
    
%     
% for i = 1 : n_sides
%         
%         j = 2;
%         u = unitaryVectors(i,:) ; 
%         u(4) = 1;
%         x = position(i,1);
%         y = position(i,2);
%         z = position(i,3);
%         
%         utrans = translation(x,y,z);
%         utras = transpose(utrans);
%         V = resolution * utras ;%+ [1,1,0];
%         disp("V...")
%         V = transpose(V);
%         disp(V);
%         disp(position(1,:))
%         plot3(V(1),V(2),V(3),'o','Color',[1 0 1],'MarkerSize',...
%              5,'MarkerFaceColor',[1 0 1]);
%          V = j*V;
%          plot3(V(1),V(2),V(3),'o','Color',[1 0 1],'MarkerSize',...
%              5,'MarkerFaceColor',[1 0 1]);
%         while magnitude == false
%             
%             if norm(V) <= mag(i)
%                 V = j*V ;
%                 pointsMatrix(j,:) = V;
%             else
%                 magnitude = true;   %Overpass or the vector reach the desired Magnitude
% 
%             end   
%             j = j + 1;
%         end  
%         
%         %Writing the points ...
%         for k = 1 : j            
%             plot3(pointsMatrix(k,1),pointsMatrix(k,2),pointsMatrix(k,3),'o','Color',[1 0 1],'MarkerSize',...
%             5,'MarkerFaceColor',[1 0 1]);            
%         end
%         
%     end
    
%     disp("Unitary Vectors ...")
%     disp(unitaryVectors); 
    
end


function cube(v1,v2,v3,v4,deltaX,res,h)
       

    numberOfPlanes = h/(res/2) ;
    disp("#PLANES ==== "+ numberOfPlanes);
    numberOfLines = norm(v4 - v3)/deltaX ;
    v3Temp = v3;
    v1Temp = v1;
    
    for j = 1 : numberOfPlanes
        
        % Writing N parallel lines 
        r_0 = v3;
        r = v1;
        disp("NumberOfLines ="+numberOfLines)
        % Considering the plane z = 0 (This code block needs to be generalized for tilted planes)
        for i = 1 : numberOfLines + 1

            lineConstruction(r_0,r,res,7)
            hold on
            v3(1) = r_0(1) + deltaX;
            v1(1) = r(1) + deltaX ;        
            r_0 = v3;
            r = v1;
        end
        
        v3 = v3Temp;
        v1 = v1Temp;
        v3(3) = res/2 + v3(3); 
        v1(3) = res/2 + v1(3);
        v3Temp = v3;
        v1Temp = v1;
        
    end

end

function lineConstruction(R_0,R, res,figNum)


    r = R;     % final point
    r_0 = R_0;   % initial point 
    t = 0;           % line parameter
    
    figure(figNum)
    writingLine(r,r_0,t);  %initial point
    xlabel("X ($\mu m$)")
    ylabel("Y($\mu m$)")
    zlabel("Z($\mu m$)")
    title("3D structure")
    xlim([-120,120]);
    ylim([-120,120]);
    zlim([-40,40]);
    grid on
    hold on
    
    counterLine = 1;
    resolution = res;    %line resolution
    
    % computing the number of points  between r_0 and r     
    numberOfPoints = norm(r - r_0)/resolution ;
    disp("Number of points on the line = "+ numberOfPoints)
    for i = 1 : numberOfPoints    
        
        t2 = resolution*i ;
        % Distance between each point (line resolution)
        if counterLine == 1
            vector =   writingLine(r,r_0,t2) - r_0 ;
            disp("Magnitud = "+ norm(vector));
        end        
        writingLine(r,r_0,t2); 
        counterLine = counterLine + 1;
        %pause(.1);
    end


end

function v =  writingLine(r,r_0,t)

    d = r - r_0 ; 
    d = d/norm(d) ;
    f = d*t + r_0 ; 
    plot3(f(1),f(2),f(3));
   
    
    if t == 0 
        plot3(f(1),f(2),f(3),'.','Color','r','MarkerSize',...
        5,'MarkerFaceColor','r');  %-o
    else
        plot3(f(1),f(2),f(3),'.','Color','b','MarkerSize',...
        5,'MarkerFaceColor','b');        
    end
    v = f;
end

function uNew = translation(x,y,z,u)
    
        sz = size(u);
        t_z = z;
        t_x = x;
        t_y = y;
        T = [1,0,0,t_x;0,1,0,t_y;0,0,1,t_z;0,0,0,1]; % Transformation Matrix T....
        
        if sz(1) > 1
            uNew = T * u ;           
        else
            uNew = T * transpose(u);
        end

end