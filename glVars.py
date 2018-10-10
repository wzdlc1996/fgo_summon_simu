# -*- coding: utf-8 -*-
import fgosummon_simu_module as fsm

helpDoc = ("Following functions have been realized: \n"
           "\'/callBot -version\' : show the version number \n"
           "\'/callBot -help\' : show the basic help doc \n"
           "\'/callBot -dice n\' : cast a n-faced dice \n"
           "\'/callBot -summon\' : Get a 10-summon \n"
           "\'/callBot -cbasummon\' : Get a 10-summon in CBA pool \n"
           "\'/callBot -FDusummon\' : Get a anniversary 2019 in 3-knight pool \n"
           "\'/callBot -FDdsummon\' : Get a anniversary 2019 in 4-knight pool \n"
           "\'/callBot -query--tot\' : Get total result statistics \n"
           "\'/callBot -query--all\' : Get all member result statistics \n"
           "\'/callBot -query--self\' : Get member-self result statistics \n"
           "\'/callBot -query--lucky\' : Get the luckiest one \n"
           "\'/callBot -query--craft\' : Get the detail of up-craft \n"
           )


s5Rate = 70
s4Rate = 50
s3Rate = 10
pickUpServ5 = ["179"];
serv5 = ["002", "008", "037", "052", "059", "060", "062", "065", "075", "076", "084", "085", "097", "113", "118", "143", "169"];
pickUpServ4 = ["180", "181"];
serv4 = ["006", "010", "011", "014", "018", "029", "030", "041", "046", "047", "048", "058", "066", "074", "082", "087", "089", "094", "100", "101", "109", "116", "120", "121", "140", "145", "146", "158", "159", "165", "170", "171"];
pickUpServ3 = [];
serv3 = ["007", "009", "013", "015", "017", "020", "022", "023", "026", "027", "028", "031","035", "042", "049", "055", "056", "063", "064", "071", "072", "079", "080", "081", "095", "104", "105", "110", "117", "124", "125"];

tmpserv5u = ['2', '8','12','59','60','68','70','76','77','84','85','88','90','91','93','96','106','119','128','129','142','143','153','156','160','173', '196']
tmpserv4u = ['6',
 '10',
 '11',
 '14',
 '18',
 '87',
 '101',
 '121',
 '140',
 '146',
 '165',
 '184',
 '193']
tmpserv3u = ['7',
 '9',
 '13',
 '15',
 '17',
 '20',
 '22',
 '63',
 '64',
 '71',
 '72',
 '95',
 '105',
 '125',
 '126',
 '148',
 '186']
tmpserv5d = ['37',
 '51',
 '52',
 '62',
 '65',
 '75',
 '86',
 '97',
 '98',
 '99',
 '108',
 '112',
 '113',
 '114',
 '118',
 '127',
 '136',
 '139',
 '144',
 '150',
 '154',
 '155',
 '161',
 '163',
 '167',
 '169',
 '175',
 '179',
 '189',
 '195']
tmpserv4d = ['29',
 '30',
 '41',
 '46',
 '47',
 '48',
 '58',
 '66',
 '74',
 '82',
 '89',
 '94',
 '100',
 '109',
 '116',
 '120',
 '145',
 '159',
 '170',
 '171',
 '185',
 '192']
tmpserv3d = ['23',
 '26',
 '27',
 '28',
 '31',
 '32',
 '35',
 '38',
 '42',
 '49',
 '55',
 '56',
 '79',
 '80',
 '81',
 '104',
 '110',
 '117',
 '124',
 '172']
cbaserv5up = ['215']
cbaserv5 = ["002", "008", "037", "052", "059", "060", "062", "065", "075", "076", "084", "085", "097", "113", "118", "143", "169", "189", "201", "206", "212"]
cbaserv4up = []
cbaserv4 = ["006", "010", "011", "014", "018", "029", "030", "041", "046", "047", "048", "058", "066", "074", "082", "087", "089", "094", "100", "101", "109", "116", "120", "121", "140", "145", "146", "158", "159", "165", "170", "171", "183", "184", "185","192","193","202","207","214"]
cbaserv3up = []
cbaserv3 = ["007", "009", "013", "015", "017", "020", "022", "023", "026", "027", "028", "031","035", "042", "049", "055", "056", "063", "064", "071", "072", "079", "080", "081", "095", "104", "105", "110", "117", "124", "125", "186", "203"]



pool = fsm.pool(serv5,pickUpServ5,serv4,pickUpServ4,serv3,pickUpServ3,cft=1,cftup=["652"])
poolFDu = fsm.pool(sv5=tmpserv5u,sv4=tmpserv4u,sv3=tmpserv3u,cft=1)
poolFDd = fsm.pool(sv5=tmpserv5d,sv4=tmpserv4d,sv3=tmpserv3d,cft=1)
poolcba = fsm.pool(cbaserv5,cbaserv5up,cbaserv4,cbaserv4up,cbaserv3,cbaserv3up)
stat = fsm.summonStat()
