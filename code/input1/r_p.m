digits(64)
fname = './avec';
avec_array = load(fname);
timestep = avec_array(:,end);
p = figure;
plot(timestep, avec_array(:,1));
print(p, 'avec', '-dpdf');
close(p);

fname = './e';
% e_array = load(fname);
% timestep = e_array(:,end);
q = figure;
% plot(timestep, e_array(:,1:3));
hold on;

fname = './eal';
d_e_array = load(fname);
timestep = d_e_array(:,end);
plot(timestep, d_e_array(:,1:6));
% legend('total potential energy', 'total kinetic energy', 'total energy',...
% 'total p atomic', 'total k atomic', 'total atomic',...
% 'total p lattic', 'total k lattic', 'total lattic',...
% 'Location', 'bestoutside');
print(q, 'energy', '-dpdf');
close(q)
