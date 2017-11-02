function WriteLog(logsout, output_path, all_samples, perm)
% Writes the log data to file
% Shows it also in command line

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                  Q G E N                                   %
%                                                                            %
%                      Copyright (C) 2011-2017, AdaCore                      %
%                      Copyright (C) 2011-2017, IB Krates                    %
%                                                                            %
%  This is free software;  you can redistribute it  and/or modify it  under  %
%  terms of the  GNU General Public License as published  by the Free Soft-  %
%  ware  Foundation;  either version 3,  or (at your option) any later ver-  %
%  sion.  This software is distributed in the hope  that it will be useful,  %
%  but WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHAN-  %
%  TABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public  %
%  License for  more details.  You should have  received  a copy of the GNU  %
%  General  Public  License  distributed  with  this  software;   see  file  %
%  COPYING3.  If not, go to http://www.gnu.org/licenses for a complete copy  %
%  of the license.                                                           %
%                                                                            %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



    if strcmp(class(logsout), 'Simulink.SimulationData.Dataset')
        write_log_dataset(logsout);
    else
        write_log_modeldatalogs(logsout);
    end
