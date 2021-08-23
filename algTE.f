      program photonics1D
      use modprob6
      implicit none

      character*50,nombre,au1
      complex*16, dimension(2,2)::MStotal,MA,MAI,MP,Ident
      DOUBLE PRECISION::w,Ref,Tra,m2,At,Lt,Ang,fi,ff
      complex*16::TrM
      integer::m,j,g,l,mm,rrrr,nang,ran_fre,Nf,NTP
      complex*16::cocairN,coc1air,coc1N,coc,coc2
      integer,dimension(:),allocatable::Aper,ANp
      DOUBLE PRECISION,dimension(:),allocatable::Aanc
      DOUBLE PRECISION,dimension(:,:),allocatable::Apar
      integer::per,Npp,capas,NUM_LINES,IOS,cap,I
      DOUBLE PRECISION::anc
      DOUBLE PRECISION,dimension(5)::par
      
      Ident(:,:)=0
      Ident(1,1)=1
      Ident(2,2)=1


     


      
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
!Secuencia lectura de archivos con la informacion de la estructura
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      OPEN (UNIT=9, FILE="CTETMF.esf", STATUS='OLD', ACCESS='SEQUENTIAL'
     &,FORM='FORMATTED', ACTION='READ' )
      IOS=0
      NUM_LINES=0
      DO I=1, 1000
	READ(9,*,IOSTAT=IOS) AU1
	IF (IOS.NE.0) GO TO 10
	NUM_LINES = NUM_LINES + 1
      END DO
10    CONTINUE
      close(unit=9)
      
      !print*,NUM_LINES

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!Finaliza la lectura del archivo
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

      OPEN (UNIT=9, FILE="CTETMF.esf", STATUS='OLD', ACCESS='SEQUENTIAL'
     &,FORM='FORMATTED', ACTION='READ' )
      
      read(9,*)nombre
      read(9,*)ran_fre
      if (ran_fre.eq.1) then
      read(9,*)fi
      read(9,*)ff
      fi=fi*1e12
      ff=ff*1e12
      else
      if (ran_fre.eq.2) then
      read(9,*)fi
      read(9,*)ff
      fi=fi*1e9
      ff=ff*1e9
      end if
      end if
      read(9,*)Nf
      read(9,*)NTP
      read(9,*)capas
      !print*,capas
      allocate (Aanc(capas))
      allocate (Aper(capas))
      allocate (Apar(capas,5))
      allocate (ANp(capas))

      open(unit=1,file=trim(adjustl(nombre))//'-TE.dat',action="write"
     &,status="unknown")!abre los archivos donde van los datos con el nombre de la estructura
      close (unit=1)

      
      open(unit=1,file=trim(adjustl(nombre))//'-TE.dat',action="write"
     &,status="replace")!abre los archivos donde van los datos con el nombre de la estructura
      


      do cap=1,capas
      read(9,*)Aanc(cap)
      read(9,*)Aper(cap)
      if (Aper(cap).eq.1) then
      read(9,*)Apar(cap,1)
      read(9,*)Apar(cap,2)
      else
      if (Aper(cap).eq.2) then
      read(9,*)Apar(cap,1)
      read(9,*)Apar(cap,2)
      read(9,*)Apar(cap,3)
      else 
      if (Aper(cap).eq.3) then
      read(9,*)Apar(cap,1)
      read(9,*)Apar(cap,2)  
      if (ran_fre.eq.1) then
      Apar(cap,2)=Apar(cap,2)*1e9*2*Pi
      else
      if (ran_fre.eq.2) then
      Apar(cap,2)=Apar(cap,2)*1e12*2*Pi     
      end if
      end if
      end if
      end if
      end if
      read(9,*)ANp(cap)
      end do
      
      close(unit=9)
      
      !print*,"ancho= ",Aanc
      !print*,"perfil= ",Aper
      !print*,"parametros= ",Apar(:,:)
      !print*,ANp


      !do rrrr=1,Nc
      !print*,ep(rrrr,wp,wp),aj(rrrr),mu(rrrr,w,wp),rrrr
      !end do
      !read*,


      open(unit=3,file='progreso.dat',action="write"
     &,status="unknown")!archivo sobre el progreso del calculo
      close (unit=3)

      
      
      
      
      
      do nang=0,Na
      Ang=Angi+(Angf-Angi)*nang/Na
      !Ang=0

      if (nang.eq.int(Na/4)) then
      print*,"25%"
      end if
      if (nang.eq.int(Na/2)) then
      print*,"50%"
      end if
      if (nang.eq.int(3*Na/4)) then
      print*,"75%"
      end if

      open(unit=3,file='progreso.dat',action="write"
     &,status="replace")
      write(3,*)"50"
      close(unit=3)
      

      MP(:,:)=0
      
      do m = 0, Nf
      w =(fi+(ff-fi)*real(m)/real(Nf))*2*Pi
      
      MStotal(1,1)=1
      MStotal(1,2)=0
      MStotal(2,1)=0
      MStotal(2,2)=1

      do cap=1,capas !capas
      anc=Aanc(cap)
      per=Aper(cap)
      par(:)=Apar(cap,:)
      Npp=ANp(cap)

      do j=1,Npp

      MA(1,1)=Qj(per,par,Npp,anc,j,w,Ang)+Qair(w,Ang)
      MA(1,2)=Qj(per,par,Npp,anc,j,w,Ang)-Qair(w,Ang)
      MA(2,1)=MA(1,2)
      MA(2,2)=MA(1,1)

      MAI(1,1)=MA(1,1)
      MAI(2,2)=MA(1,1)
      MAI(1,2)=-MA(1,2)



      MAI(2,1)=-MA(1,2)
      MAI=0.25*(1/(Qj(per,par,Npp,anc,j,w,Ang)*Qair(w,Ang)))*MAI
      
      MP(1,1)=Exp(im*Qj(per,par,Npp,anc,j,w,Ang)*aj(Npp,anc))
      MP(2,2)=Exp(-im*Qj(per,par,Npp,anc,j,w,Ang)*aj(Npp,anc))
      
      MStotal=matmul(matmul(MAI,matmul(MP,MA)),MStotal)
     
      end do


      
      end do !capas

     

      TrM=MStotal(1,1)+MStotal(2,2)
      MStotal=poli(NTP-1,TrM)*MStotal-poli(NTP-2,TrM)*Ident

      Ref=abs(-MStotal(2,1)/MStotal(2,2))
      Tra=abs(1/MStotal(2,2))

      Ref=abs(Ref)**2
      Tra=abs(Tra)**2
      
      !print*,w/(2*Pi)/1e12,Ref+Tra
      
      if (ran_fre.eq.1) then
      write(1,*)Ang*180/Pi,w/(2*Pi)/1e12,Ref,Tra,Ref+Tra
      else
      if (ran_fre.eq.2) then
      write(1,*)Ang*180/Pi,w/(2*Pi)/1e9,Ref,Tra,Ref+Tra
      end if
      end if

      end do
      write(1,*)
    
      
      end do
      print*,"Fin modo TE"
      
      close(unit=1)
     
      
      
      end program

