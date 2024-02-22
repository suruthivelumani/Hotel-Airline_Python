#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<fstream.h>
#include<process.h>
class flight
{
int fprice,ftype,fbill,nooftickets;
char fname[25],farvl[75],fdept[50],date[10],fdur[25],fid[5];
void fprice1()
{
if(ftype==1)
{
strcpy(fdept,"Indira Gandhi International Airport, Delhi");
fprice=4215;
strcpy(fdur,"2 hrs 40 mins");
}
else if(ftype==2)
{
strcpy(fdept,"Chhatrapati Shivaji International Airport, Mumbai");
fprice=2549;
strcpy(fdur,"1 hrs 20 mins");
}
else if(ftype==3)
{
strcpy(fdept,"Kempegowda International Airport, Bangalore");
fprice=2690;
strcpy(fdur,"1 hrs 20 mins");
}
else if(ftype==4)
{
strcpy(fdept,"Chennai International Airport, Chennai");
fprice=3311;
strcpy(fdur,"2 hrs 5 mins");
}
else if(ftype==5)
{
strcpy(fdept,"Netaji Subhas Chandra Bose International Airport, Kolkata");
fprice=8994;
strcpy(fdur,"3 hrs 15 mins");
}
else if(ftype==6)
{
strcpy(fdept,"Rajiv Gandhi International Airport, Hyderabad");
fprice=2880;
strcpy(fdur,"1 hrs 30 mins");
}
else if(ftype==7)
{
strcpy(fdept,"Cochin International Airport, Kochi");
fprice=5942;
strcpy(fdur,"2 hrs 55 mins");
}
else if(ftype==8)
{
strcpy(fdept,"Sardar Vallabhbhai Patel International Airport, Ahmedabad");
fprice=3410;
strcpy(fdur,"1 hrs 55 mins");
}
else if(ftype==9)
{
strcpy(fdept,"Lokpriya Gopinath Bordoloi International Airport, Guwahati");
fprice=10268;
strcpy(fdur,"5 hrs 20 mins");
}
fbill=fprice*nooftickets;
}
public:
flight()
{  fbill=0;
strcpy(farvl,"Goa International Airport, Goa");
}
void fgetinfo()
{   clrscr();
cout<<"Enter ID"<<endl;
cin>>fid;
cout<<"Enter your name"<<endl;
gets(fname) ;
cout<<"Enter no. of tickets"<<endl;
cin>>nooftickets;
cout<<"Enter date of travel"<<endl;
gets(date);
cout<<"Choose your depature airport"<<endl;
cout<<"  1)   Indira Gandhi International Airport, Delhi"<<endl;
cout<<"  2)   Chhatrapati Shivaji International Airport, Mumbai"<<endl;
cout<<"  3)   Kempegowda International Airport, Bangalore"<<endl;
cout<<"  4)   Chennai International Airport, Chennai"<<endl;
cout<<"  5)   Netaji Subhas Chandra Bose International Airport, Kolkata"<<endl;
cout<<"  6)   Rajiv Gandhi International Airport, Hyderabad"<<endl;
cout<<"  7)   Cochin International Airport, Kochi"<<endl;
cout<<"  8)   Sardar Vallabhbhai Patel International Airport, Ahmedabad"<<endl;
cout<<"  9)   Lokpriya Gopinath Bordoloi International Airport, Guwahati"<<endl;
cout<<"Press any no. between 1 and 9"<<endl;
cin>>ftype;
fprice1();
}
void fshowinfo()
{
cout<<"ID                             :  "<<fid<<endl;
cout<<"Name                      :  "<<fname<<endl;
cout<<"No of tickets          :  "<<nooftickets<<endl;
cout<<"Date of travel        :  "<<date<<endl;
cout<<"Departure              :  "<<fdept<<endl;
cout<<"Arrival                     :  "<<farvl <<endl;
cout<<"Duration                 :  "<<fdur<<endl;
cout<<"Bill                           :  "<<fbill<<endl;
}
char *retfid()
{return fid;}
void fmod()
{
clrscr();
cout<<"Enter your name"<<endl;
gets(fname) ;
cout<<"Enter no. of tickets"<<endl;
cin>>nooftickets;
cout<<"Enter date of travel"<<endl;
gets(date);
cout<<"Choose your depature airport"<<endl;
cout<<"  1)   Indira Gandhi International Airport, Delhi"<<endl;
cout<<"  2)   Chhatrapati Shivaji International Airport, Mumbai"<<endl;
cout<<"  3)   Kempegowda International Airport, Bangalore"<<endl;
cout<<"  4)   Chennai International Airport, Chennai"<<endl;
cout<<"  5)   Netaji Subhas Chandra Bose International Airport, Kolkata"<<endl;
cout<<"  6)   Rajiv Gandhi International Airport, Hyderabad"<<endl;
cout<<"  7)   Cochin International Airport, Kochi"<<endl;
cout<<"  8)   Sardar Vallabhbhai Patel International Airport, Ahmedabad"<<endl;
cout<<"  9)   Lokpriya Gopinath Bordoloi International Airport, Guwahati"<<endl;
cout<<"Press any no. between 1 and  9"<<endl;
cin>>ftype;
fprice1();
}
};






void fbook()
{  clrscr();
flight f;
ofstream fout;
fout.open("flight.dat",ios::binary|ios::app);
f.fgetinfo();
fout.write((char*)&f,sizeof(f));
cout<<"Booking over"<<endl;
cout<<"Thanking you for using our service!"<<endl;
fout.close();
}







void fmodify()
{    char gid[5];
clrscr();
flight f;
cout<<"Enter ID to modify booking"<<endl;
cin>>gid;
fstream fio;
fio.open("flight.dat",ios::binary|ios::in|ios::out,ios::app);
while(fio.read((char*)&f,sizeof(f)))
{
if(strcmp(gid,f.retfid())==0)
{
f.fmod();
fio.seekp(-1*sizeof(f),ios::cur);
fio.write((char*)&f,sizeof(f));
}
}fio.close();
cout<<"Booking modified"<<endl;
cout<<"Thanking you for using our service!"<<endl;
}







void fcancel()
{    char gid[5];
clrscr();
flight f;
cout<<"Enter ID to cancel booking"<<endl;
cin>>gid;
ifstream fin;
ofstream fout;
fin.open("flight.dat",ios::binary);
fout.open("tempf.dat",ios::binary);
while(fin.read((char*)&f,sizeof(f)))
{
if(strcmp(gid,f.retfid())!=0)
fout.write((char*)&f,sizeof(f));
}
remove("flight.dat");
rename("tempf.dat","flight.dat");
fin.close();
fout.close();
cout<<"Booking cancelled"<<endl;
cout<<"Thanking you for using our service!"<<endl;
}









void fview()
{   char gid[5];
clrscr();
flight f;
cout<<"Enter ID to view booking"<<endl;
cin>>gid;
ifstream fin;
fin.open("flight.dat",ios::binary);
while(fin.read((char*)&f,sizeof(f)))
{
if(strcmp(gid,f.retfid())==0)
{
f.fshowinfo();
}
}
fin.close();
cout<<"Booking viewed"<<endl;
cout<<"Thanking you for using our service!"<<endl;
}


















class hotel
{   char name[25],rmtype[10],id[5];
int rtype,noofrms,noofdays,rprice,rbill;
char checkindate[8],checkoutdate[8];
void price()
{
if(rtype==1)
{
strcpy(rmtype,"Standard");
rprice=3658;
}
else if(rtype==2)
{
strcpy(rmtype,"Executive");
rprice=7544;
}
else if(rtype==3)
{
strcpy(rmtype,"Club");
rprice=12432;
}
rbill=rprice*noofrms*noofdays;
}
public:
hotel()
{
strcpy(name,"NULL");
rtype=0;
rprice=0;
rbill=0;
}
void hgetinfo()
{
cout<<"Enter id"<<endl;
cin>>id;
cout<<"Enter ur name"<<endl;
gets(name);
cout<<"Enter checkindate (dd/mm/yy)"<<endl;
cin>>checkindate;
cout<<"Enter checkoutdate (dd/mm/yy)"<<endl;
cin>>checkoutdate;
cout<<"Enter no. of days of stay"<<endl;
cin>>noofdays;
cout<<"Enter no of rooms"<<endl;
cin>>noofrms;
cout<<"Choose the roomtype"<<endl;
cout<<"     1)   Standard "<<endl;
cout<<"     2)   Executive "<<endl;
cout<<"     3)   Club  "<<endl;
cout<<"Press 1 or 2 or 3"<<endl;
cin>>rtype;
price();
}
void hshowinfo()
{
cout<<"ID                          :   "<<id<<endl;
cout<<"Name                   :   "<<name<<endl;
cout<<"Check-in date     :   "<<checkindate<<endl;
cout<<"Check-out date :   "<<checkoutdate<<endl;
cout<<"No. of days         :   "<<noofdays<<endl;
cout<<"No. of rooms     :   "<<noofrms<<endl;
cout<<"Room type         :   "<<rmtype<<endl;
cout<<"Total bill             :   "<<rbill<<endl;
}
 char *retid()
 { return id;}
 void hmod()
 {
 clrscr();
cout<<"Enter your name"<<endl;
gets(name);
cout<<"Enter check-in date (dd/mm/yy)"<<endl;
cin>>checkindate;
cout<<"Enter check-out date (dd/mm/yy)"<<endl;
cin>>checkoutdate;
cout<<"Enter no. of days of stay"<<endl;
cin>>noofdays;
cout<<"Enter no. of rooms"<<endl;
cin>>noofrms;
cout<<"Choose the roomtype"<<endl;
cout<<"     1)   Standard "<<endl;
cout<<"     2)   Executive "<<endl;
cout<<"     3)   Club  "<<endl;
cout<<"Press 1 or 2 or 3"<<endl;
cin>>rtype;
price();
}
};
void hbook()
{
clrscr();
hotel h;
ofstream fout;
fout.open("hotel.dat" ,ios::binary|ios::out|ios::app);
h.hgetinfo();
fout.write((char*)&h ,sizeof(h));
fout.close();
cout<<"Booking over"<<endl;
cout<<"Thanking you for using our service!"<<endl;
}
void hmodify()
{
clrscr();
hotel h;
char sid[5];
cout<<"Enter ID to modify booking"<<endl;
cin>>sid;
fstream f;
f.open("hotel.dat",ios::binary|ios::in|ios::out|ios::app);
while(f.read((char*)&h ,sizeof(h)))
{
if(strcmp(h.retid(),sid)==0)
{
h.hmod();
f.seekp(-1*sizeof(h),ios::cur);
f.write((char*)&h,sizeof(h));
}
}
f.close();
cout<<"Booking modified"<<endl;
cout<<"Thanking you for using our service!"<<endl;
}
void hview()
{
clrscr();
hotel h;
char sid[5];
cout<<"Enter ID to view booking"<<endl;
cin>>sid;
ifstream fin;
fin.open("hotel.dat" ,ios::binary|ios::in);
while(fin.read((char*)&h ,sizeof(h)))
{
if(strcmp(h.retid(),sid)==0)
h.hshowinfo();
}
fin.close();
cout<<"Booking viewed"<<endl;
cout<<"Thanking you for using our service!"<<endl;
}

void hcancel()
{
clrscr();
hotel h;
char sid[5];
cout<<"Enter ID to view booking"<<endl;
cin>>sid;
ifstream fin;
ofstream fout;
fin.open("hotel.dat" ,ios::binary|ios::in);
fout.open("temph.dat",ios::binary|ios::out);

while(fin.read((char*)&h ,sizeof(h)))
{
if(strcmp(h.retid(),sid)!=0)
{fout.write((char*)&h,sizeof(h));}
}
fin.close();
fout.close();
remove("hotel.dat");
rename("temph.dat","hotel.dat");
cout<<"Booking cancelled"<<endl;
cout<<"Thanking you for using our service!"<<endl;
}



