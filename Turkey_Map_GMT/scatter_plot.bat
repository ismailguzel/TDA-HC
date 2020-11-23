@echo OFF
set proj=-JM0/0/15.00c
set frm=-Bs2 -BWSen
set lim=-R25.69/45.01/34.49/42.21
set ps=Turkey_Cities.ps

REM ----- Plot maps
psbasemap %lim% %proj% %frm% -X2.5c -Y2.5c  -K > %ps%
pscoast -Df -N1/0.25p -W0.25p,0/0/0 -S255/255/255 -G230/230/230 %lim% %proj% %frm% -A1000  -O -K >> %ps%

REM  ---- Plot symbols
psxy cities_label.txt -C0/0/0 -Sc4p -Gred -R -J -O -K>> %ps%

REM  ---- Plot colorbar
pstext -J -R cities_label.txt -F+f8p,Helvetica,black -D0.0/0.2 -O >> %ps%

REM Convert to PNG
psconvert *.ps -A -P -Tg

del *.ps
del *.history
pause