
bday=["birthday","bday"]
disc = ["a","an","the","of","is","was","in","during","got","are","did","took","belongs","to","has","at","on","and"
        ,"or","me","celebrated","celebrate","regarding","into","came","action","existence","exist","rule","legal","become"
	,"became","does","political","records","any","home","located","total","how","much","with","my","based","as","being"
	,"done","found","under","can","you","get","for","offered","offer","by","many","that","have","draw","it","so","draws"
	,"whome","included","include","through","go","said","happened","whom","whose","who","this","water","body","neft","having"
	,"what","overall","moving","travelling","travel","go","going","goes","moves"
	,"if","then","than","be","could","been","weapon","belong"
        ,"shown","hit","come","happen","strike","earthquake","related","relate","relates","relating","called","tell","known"
	, "famous","famously","prize","national","most","read","both","record","recorded","live","will","goes","stretch","run","over",
	  "pass","through","number","numbers","where","from","performed","won","olympics","university","talks","were","when","which"]
bank = ["bank"]
minister = ["minister","ministers"]
theatre = ["theatre","theater","showtime","shows","showing","theaters","theatres","timing"]
meaning = ["means","define","definition","meaning","mean","meant"]
std = ["std code","stdcode"]
cric_info = ["cricketer","cricket player","cric player","cric stats","cricket stats","cricket statistics","cric statistics","batsmen","batter","bowler"]
t = ["train","trains","passenger","express"]
w = ["weather","weathers","climate","climates","climatic"]
s = ["stock","stocks"]
e = ["exam","examination","exams","examinations","test","tests"]
m = ["gold","silver","oil","petrol"]
r = ["movie","director","cast","writer","producer","story","release","genre","rating","music","cinematographer","editor","review"]
loc = ["near","around","close","closest","nearest"]
mov = ["movie","director","cast","writer","producer","story","release","genre","rating","music","cinematographer","editor","review"]
sp = ["score","cricket"]
h = ["highway","highways"]
d = ["difference","differences","compare","comparision","comparisions","differentiate"]
low = ["less","lesser","lower","smaller"]
high = ["high","higher","more","greater"]
maxi = ["maximum","highest","tallest","largest","longest"]
mini = ["minimum","least","smallest","tiniest","deepest"]
avg = ["average","mean"]
summ = ["total","sum","aggregate"]
ordins = ["hundred","thousand","million","billion","trillion","lakh","crore"]
normal = {"one":"first","two":"second","three":"third","four":"fourth","five":"fifth","six":"sixth",
	  "seven":"seventh","eight":"eighth","nine":"ninth","ten":"tenth","eleven":"eleventh","twelve":"twelfth","thirteen":"thirteenth",
	  "fourteen":"fourteenth","fifteen":"fifteenth","sixteen":"sixteenth","seventeen":"seventeenth","eighteen":"eighteenth", 		  "ninteen":"ninteenth","twenty":"twentieth","thirty":"thirtieth","forty":"fortieth","fifty":"fiftieth","sixty":"sixtieth",
	  "seventy":"seventieth","eighty":"eightieth","ninty":"ninetieth","hundred":"hundredth","thousand":"thousandth","million":"millionth",
	  "billion":"billionth","trillion":"trillionth","lakh":"lakth","crore":"croreth"}
endins = ["st","nd","rd","th"]
extras = ["and"]
totalnum = []
totalnum.extend(normal.keys())
totalnum.extend(normal.values())
totalnum.extend(extras)
calender = ["day","days","week","weeks","year","years","month","months","decade","century","decades","centuries"]
yearbox = ["year","years","decade","decades","century","centuries"]
negetive = ["previous","yesterday","before","back","less","earlier"]
positive = ["next","tomorrow","after","forthcoming","later","more"]
daters = []
daters.extend(calender)
daters.extend(yearbox)
daters.extend(negetive)
daters.extend(positive)
curr = {'rupiahs': 'Indonesian Rupiah', 'czech korunas': 'Czech Koruna', 'yen': 'Japanese Yen', 'dollar': 'US Dollar', 
	'us dollars': 'US Dollar', 'brazilian real': 'Brazilian Real', 'korunas': 'Czech Koruna', 'israeli shekels': 'Israeli Shekel', 
	'lats': 'Latvian Lat', 'kazakhstani tenges': 'Kazakhstani Tenge', 'russian ruble': 'Russian Ruble', 'japanese yens': 'Japanese Yen', 
	'bruneian dollars': 'Bruneian Dollar', 'forints': 'Hungarian Forint', 'litas': 'Lithuanian Litas', 'emirati dirham': 'Emirati Dirham', 
	'rands': 'South African Rand', 'lira': 'Turkish Lira', 'swedish kronas': 'Swedish Krona', 'singapore dollars': 'Singapore Dollar', 
	'real': 'Brazilian Real', 'trinidadian dollar': 'Trinidadian Dollar', 'libyan dinar': 'Libyan Dinar', 'koruna': 'Czech Koruna', 
	'danish krones': 'Danish Krone', 'pulas': 'Botswana Pula', 'argentine peso': 'Argentine Peso', 'ringgits': 'Malaysian Ringgit', 
	'iranian rials': 'Iranian Rial', 'bulgarian levs': 'Bulgarian Lev', 'norwegian krones': 'Norwegian Krone', 'mexican peso': 'Mexican Peso', 
	'tenges': 'Kazakhstani Tenge', 'israeli shekel': 'Israeli Shekel', 'singapore dollar': 'Singapore Dollar', 'wons': 'South Korean Won', 
	'south african rands': 'South African Rand', 'pounds': 'British Pound', 'polish zloty': 'Polish Zloty', 'canadian dollars': 'Canadian Dollar', 
	'nepalese rupees': 'Nepalese Rupee', 'leus': 'Romanian New Leu', 'shekels': 'Israeli Shekel', 'renminbis': 'Chinese Yuan Renminbi', 
	'thai bahts': 'Thai Baht', 'sri lankan rupees': 'Sri Lankan Rupee', 'indonesian rupiahs': 'Indonesian Rupiah', 'croatian kuna': 'Croatian Kuna', 
	'kuwaiti dinars': 'Kuwaiti Dinar', 'botswana pulas': 'Botswana Pula', 'zloty': 'Polish Zloty', 'venezuelan bolivars': 'Venezuelan Bolivar', 
	'sri lankan rupee': 'Sri Lankan Rupee', 'icelandic kronas': 'Icelandic Krona', 'latvian lat': 'Latvian Lat', 'romanian new leus': 'Romanian New Leu', 
	'pakistani rupee': 'Pakistani Rupee', 'new zealand dollar': 'New Zealand Dollar', 'litass': 'Lithuanian Litas', 'norwegian krone': 'Norwegian Krone', 
	'dinars': 'Libyan Dinar', 'bahraini dinar': 'Bahraini Dinar', 'brazilian reals': 'Brazilian Real', 'won': 'South Korean Won', 'iranian rial': 'Iranian Rial', 
	'chilean pesos': 'Chilean Peso', 'mauritian rupee': 'Mauritian Rupee', 'franc': 'Swiss Franc', 'trinidadian dollars': 'Trinidadian Dollar', 
	'krones': 'Norwegian Krone', 'forint': 'Hungarian Forint', 'baht': 'Thai Baht', 'zlotys': 'Polish Zloty', 'shekel': 'Israeli Shekel', 
	'kunas': 'Croatian Kuna', 'leu': 'Romanian New Leu', 'lev': 'Bulgarian Lev', 'renminbi': 'Chinese Yuan Renminbi', 'malaysian ringgits': 'Malaysian Ringgit', 
	'indonesian rupiah': 'Indonesian Rupiah', 'argentine pesos': 'Argentine Peso', 'danish krone': 'Danish Krone', 'euros': 'Euro', 
	'australian dollars': 'Australian Dollar', 'kuna': 'Croatian Kuna', 'hong kong dollars': 'Hong Kong Dollar', 'us dollar': 'US Dollar', 
	'francs': 'Swiss Franc', 'bruneian dollar': 'Bruneian Dollar', 'rand': 'South African Rand', 'botswana pula': 'Botswana Pula', 
	'mexican pesos': 'Mexican Peso', 'japanese yen': 'Japanese Yen', 'hong kong dollar': 'Hong Kong Dollar', 'qatari riyal': 'Qatari Riyal', 
	'canadian dollar': 'Canadian Dollar', 'colombian pesos': 'Colombian Peso', 'bolivars': 'Venezuelan Bolivar', 'chilean peso': 'Chilean Peso', 
	'pound': 'British Pound', 'pakistani rupees': 'Pakistani Rupee', 'bolivar': 'Venezuelan Bolivar', 'new zealand dollars': 'New Zealand Dollar', 
	'colombian peso': 'Colombian Peso', 'lithuanian litas': 'Lithuanian Litas', 'libyan dinars': 'Libyan Dinar', 'emirati dirhams': 'Emirati Dirham', 
	'krona': 'Swedish Krona', 'philippine peso': 'Philippine Peso', 'krone': 'Norwegian Krone', 'ruble': 'Russian Ruble', 'thai baht': 'Thai Baht', 
	'south african rand': 'South African Rand', 'australian dollar': 'Australian Dollar', 'venezuelan bolivar': 'Venezuelan Bolivar', 'swedish krona': 'Swedish Krona', 
	'kazakhstani tenge': 'Kazakhstani Tenge', 'south korean won': 'South Korean Won', 'nepalese rupee': 'Nepalese Rupee', 'croatian kunas': 'Croatian Kuna', 
	'british pounds': 'British Pound', 'rials': 'Omani Rial', 'qatari riyals': 'Qatari Riyal', 'czech koruna': 'Czech Koruna', 'hungarian forints': 'Hungarian Forint', 
	'pula': 'Botswana Pula', 'south korean wons': 'South Korean Won', 'riyal': 'Saudi Arabian Riyal', 'peso': 'Philippine Peso', 
	'turkish lira': 'Turkish Lira', 'omani rial': 'Omani Rial', 'pesos': 'Philippine Peso', 'kronas': 'Swedish Krona', 'yens': 'Japanese Yen', 
	'dollars': 'US Dollar', 'bahts': 'Thai Baht', 'omani rials': 'Omani Rial', 'bulgarian lev': 'Bulgarian Lev', 'turkish liras': 'Turkish Lira', 
	'taiwan new dollar': 'Taiwan New Dollar', 'hungarian forint': 'Hungarian Forint', 'russian rubles': 'Russian Ruble', 'romanian new leu': 'Romanian New Leu', 
	'latvian lats': 'Latvian Lat', 'polish zlotys': 'Polish Zloty', 'tenge': 'Kazakhstani Tenge', 'philippine pesos': 'Philippine Peso', 
	'bahraini dinars': 'Bahraini Dinar', 'rubles': 'Russian Ruble', 'kuwaiti dinar': 'Kuwaiti Dinar', 'chinese yuan renminbi': 'Chinese Yuan Renminbi', 
	'lithuanian litass': 'Lithuanian Litas', 'icelandic krona': 'Icelandic Krona', 'swiss francs': 'Swiss Franc', 'dirham': 'Emirati Dirham', 
	'reals': 'Brazilian Real', 'rupiah': 'Indonesian Rupiah', 'rial': 'Omani Rial', 'dirhams': 'Emirati Dirham', 'levs': 'Bulgarian Lev', 
	'liras': 'Turkish Lira', 'swiss franc': 'Swiss Franc', 'mauritian rupees': 'Mauritian Rupee', 'lat': 'Latvian Lat', 'saudi arabian riyal': 'Saudi Arabian Riyal', 
	'taiwan new dollars': 'Taiwan New Dollar', 'saudi arabian riyals': 'Saudi Arabian Riyal', 'euro': 'Euro', 'dinar': 'Libyan Dinar', 
	'chinese yuan renminbis': 'Chinese Yuan Renminbi', 'ringgit': 'Malaysian Ringgit', 'riyals': 'Saudi Arabian Riyal', 'malaysian ringgit': 'Malaysian Ringgit', 
	'british pound': 'British Pound','usd':'US Dollar','inr':'Indian Rupee','rupee':'Indian Rupee','rupees':'Indian Rupee','indian rupee':'Indian Rupee',
	'indian rupees':'Indian Rupee'}
