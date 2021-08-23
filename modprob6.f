      module modprob6
      implicit none


      DOUBLE PRECISION, parameter::c=299792458
      DOUBLE PRECISION, parameter::e0=8.8541878176e-12
      DOUBLE PRECISION, parameter::mu0=1/(e0*c*c)
      DOUBLE PRECISION, parameter::Zair=sqrt(mu0/e0)
      DOUBLE PRECISION,parameter::Pi=3.141592653589793
      
      
     

      
      
    
      complex*16, parameter::im=(0,1)
      

         
      DOUBLE PRECISION,parameter::Angi=0
      DOUBLE PRECISION,parameter::Angf=Pi/2
      integer,parameter::Na=100
      

      DOUBLE PRECISION,parameter::ch=-1.6e-19
      DOUBLE PRECISION,parameter::hb=6.58211899e-16
      DOUBLE PRECISION,parameter::kb=8.6173324e-5

      !DOUBLE PRECISION,parameter::Ang=0
      DOUBLE PRECISION,parameter::mug=0.2
      DOUBLE PRECISION,parameter::wp=2*2*pi*1e12
      DOUBLE PRECISION,parameter::wpp=3*2*pi*1e12
      DOUBLE PRECISION,parameter::T=300.
      
      contains
      
      complex*16 function sintra(w) result(r)
      implicit none
      DOUBLE PRECISION, intent(in)::w
      r=(((ch**2)*im*16*kb*T)/(4*hb*1.6e-19*2*Pi*hb*w))*log(2*cosh(mug/(
     &2*kb*T)))
      end function sintra
      
      complex*16 function sinter(w) result(r)
      implicit none
      DOUBLE PRECISION, intent(in)::w
      DOUBLE PRECISION::c1,c2,c3,c4
      c1=(ch**2)/(4*hb*1.6e-19)
      c2=2*kb*T
      c3=(hb*w+2*mug)
      c4=(hb*w-2*mug)
      r=c1*((0.5+(1/Pi)*atan(c4/c2))-(im/(2*Pi))*log((c3**2)/((c4**2)+
     &(c2**2))))
      end function sinter
      
      complex*16 function ss(w) result(r)
      implicit none
      DOUBLE PRECISION, intent(in)::w
      r=0*(sinter(w)+sintra(w))
      end function ss

      DOUBLE PRECISION function aj(Np,anc) result(r)
      implicit none
      integer, intent(in)::Np
      DOUBLE PRECISION, intent(in)::anc
      
      r=anc/Np
    
      end function aj

        
      DOUBLE PRECISION function f(per,par,x,w) result(r)
      implicit none
      DOUBLE PRECISION, intent(in)::x,w
      integer, intent(in)::per
      DOUBLE PRECISION, dimension(5)::par
      
      
      
      if (per.eq.1) then
      r=par(1)*x+par(2)
      else
      if (per.eq.2) then
      r=par(1)*Exp(par(2)*x)+par(3)
      else
      if (per.eq.3) then
      r=par(1)-(par(2)/w)**2
      end if
      end if
      end if
      end function f

      complex*16 function eps(per,par,Np,anc,j,w) result(r)
      integer, intent(in)::j,per,Np
      DOUBLE PRECISION, dimension(5)::par
      DOUBLE PRECISION, intent(in)::w,anc

      if (modulo(j,Np+1).eq.0) then
      r=f(per,par,(real(Np)-0.5)*anc/Np,w)
      else
      r=f(per,par,((modulo(j,Np+1)-1)-0.5)*anc/Np,w)
      end if

      end function eps

      
      complex*16 function Nj(per,par,Np,anc,j,w) result(r)
      integer, intent(in)::j,per,Np
      DOUBLE PRECISION, dimension(5)::par
      DOUBLE PRECISION, intent(in)::w,anc

      r=sqrt(eps(per,par,Np,anc,j,w))
      end function Nj

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111

      DOUBLE PRECISION function k0(w) result(r)
      implicit none
      DOUBLE PRECISION,intent(in)::w
      r=w/c
      end function k0

      DOUBLE PRECISION function ky(w,Ang) result(r)
      implicit none
      DOUBLE PRECISION,intent(in)::w,Ang
      r=k0(w)*Sin(Ang)
      end function ky

      complex*16 function Qair(w,Ang) result(r)
      implicit none
      DOUBLE PRECISION,intent(in)::w,Ang
      r=sqrt(k0(w)*k0(w)-ky(w,Ang)*ky(w,Ang))
      end function Qair

      complex*16 function Qj(per,par,Np,anc,j,w,Ang) result(r)
      implicit none
      integer,intent(in)::j,per,Np
      DOUBLE PRECISION,intent(in)::w,Ang,anc
      DOUBLE PRECISION, dimension(5)::par
      
      r=sqrt(k0(w)*k0(w)*Nj(per,par,Np,anc,j,w)*Nj(per,par,Np,anc,j,w)-
     &ky(w,Ang)*ky(w,Ang))
      end function Qj

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
! RUTINA POLINOMIOS 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      complex*16 function poli(n,k) result(r)
      implicit none
      integer,intent(in)::n
      complex*16,intent(in)::k
      complex*16,dimension(:),allocatable::pol
      integer::j      
      if (n<0) then
         if (n==-2) then
            r=-1  !valor especial para hacer funcionar las ecuaciones utilizadas
         else
            r=0
         end if
      else
         if (n==0) then
            r=1
         else
            allocate (pol(n+1))
            pol(1)=1
            pol(2)=k
            if (n==1) then
               r=k
            else
               do j=3,n+1
                  pol(j)=k*pol(j-1)-pol(j-2)
               end do
               r=pol(n+1)
            end if
         end if
      end if
      
      
      end function poli

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
!!!!!!  fin del modulo
!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
      end module modprob6
