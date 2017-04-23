fname = './avec';
avec_array = load(fname);
timestep = avec_array(:,end);
p = figure;
plot(timestep, avec_array(:,1));
print(p, 'avec', '-dpng');
close(p);

fname = './e';
e_array = load(fname);
timestep = e_array(:,end);
q = figure;
plot(timestep, e_array(:,1:3));
legend('total potential energy', 'total kinetic energy', 'total energy',...
'Location', 'best');
print(q, 'energy', '-dpng');
close(q)
