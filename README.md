# Python PDF redaktors

Šī Python lietojumprogramma, kas izveidota, izmantojot Tkinter bibliotēku, nodrošina lietotājam draudzīgu saskarni PDF failu sadalīšanai un apvienošanai. Tas izmanto PyPDF2 bibliotēku, lai apstrādātu PDF failu darbības.

<p align="center"><img src="https://i.imgur.com/bTDXBEH.png"/></p>

<br/><br/>

## Iespējas

##### Sadalīt PDF

- Atlasiet PDF failu, izmantojot failu dialoglodziņu.

- Norādiet lapu diapazonus, lai izvilktu un izveidotu jaunu PDF failu.

- Atbalsta ar komatu atdalītus lapu diapazonus (piem., 1-3, 5, 8-10).

##### Apvienot PDF

- Izvēlieties vairākus PDF failus, lai tos apvienotu vienā PDF failā.

- Sakārtojiet failu secību sapludināšanas sarakstā.

- Saglabājiet apvienoto PDF failu ar noteiktu nosaukumu.

##### Attēla konvertēšana uz PDF

- Atbalstītie attēlu formāti ietver JPEG, PNG, BMP un citus.

- Saglabājiet pārveidotos attēlus PDF failā ar noteiktu nosaukumu.

##### Attēla ekstraktēšana no PDF

- Saglabājiet pārveidotos attēlus no PDF izvēlētājā direktorijā.

<br/>

## Darba sākšana

1. Pārliecinieties, vai jūsu datorā ar Tkinter ir instalēts Python 3.x.

2. Instalējiet vajadzīgās bibliotēkas, izmantojot šādu komandu: `pip install -r prasības.txt`

3. Palaidiet Python skriptu python python-pdf-editor.py, lai palaistu lietojumprogrammu.
<br/>

## Lietošanas instrukcijas

##### Sadalīt cilne

1. Noklikšķiniet uz pogas "+", lai atlasītu PDF failu.

2. Ievadiet lappušu diapazonus formātā (piemēram, 1-3, 5, 8-10).

3. Noklikšķiniet uz pogas "Split".

4. Izvēlieties vietu, kur saglabāt jauno PDF failu.

##### Apvienot cilne

1. Noklikšķiniet uz pogas "+", lai sapludināšanas sarakstam pievienotu PDF failus.

2. Noņemiet no saraksta nevēlamos PDF failus, izveloties, un spiežot pogu DELETE.

3. Noklikšķiniet uz pogas "Merge".

4. Izvēlieties vietu, kur saglabāt apvienoto PDF failu.

##### Attēli uz PDF cilne

1. Noklikšķiniet uz pogas "+", lai sarakstam pievienotu attēla failus.

2. Noņemiet no saraksta nevēlamos attēla failus, izveloties, un spiežot pogu DELETE.

3. Noklikšķiniet uz pogas "Convert".

4. Izvēlieties vietu, kur saglabāt PDF failu.

##### Attēlu ekstraktēšanas cilne

1. Noklikšķiniet uz pogas "+", lai atlasītu PDF failu.

2. Noklikšķiniet uz pogas "Extract".

3. Izvēlieties vietu, kur saglabāt attēlus no PDF.
<br/>

## Lietotās bibliotēkas

- **Tkinter**: Tkinter ir standarta GUI (grafiskā lietotāja interfeisa) rīkkopa, kas tiek komplektēta ar Python. Tas nodrošina rīku komplektu intuitīvu un interaktīvu grafisko saskarņu izveidei, padarot to par ideālu izvēli darbvirsmas lietojumprogrammu izstrādei.

- **PyPDF2**: PyPDF2 ir Python bibliotēka, kas īpaši izstrādāta darbam ar PDF failiem. Tas ļauj lietojumprogrammai lasīt, apstrādāt un rakstīt PDF dokumentus. PyPDF2 iespējas ietver vairāku PDF failu sapludināšanu, PDF failu sadalīšanu, pamatojoties uz norādītajiem lappušu diapazoniem, un daudz ko citu.

- **pypdf**: Pypdf ir bibliotēka, kura tiek izmantota, lai pārvarētu PyPDF2 ierobežojumus, īpaši caurspīdīgai attēlu iegūšanai, jo PyPDF2 nenodrošina tiešu atbalstu šai funkcijai.

- **img2pdf**: Img2pdf ir bibliotēka, ko izmanto attēlu konvertēšanai PDF formātā. Šajā projektā to izmanto attēlu datu konvertēšanai PDF formātā pirms apvienošanas.

- **io**: Modulis "io" ir Python standarta bibliotēkas daļa un nodrošina rīkus darbam ar straumēm un ievades/izvades darbībām. Tas tiek izmantots šajā projektā, lai izveidotu straumi no binārajiem datiem PyPDF2 bibliotēkai.

- **os**: Modulis "os" ir Python standarta bibliotēkas daļa un nodrošina veidu, kā mijiedarboties ar operētājsistēmu. Šajā projektā tas tiek izmantots ar failiem saistītām darbībām, piemēram, faila esamības pārbaudei un failu ceļu pārvaldībai.