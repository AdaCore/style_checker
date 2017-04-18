/****************************************************************************
 *                                                                          *
 *                          ESA RAVENSCAR BENCHMARK                         *
 *                                                                          *
 *                             S U P P O R T . C                            *
 *                                                                          *
 *                        Copyright (C) 2006, AdaCore                       *
 *                                                                          *
 * The ESA  Ravenscar Benchmark is free  software;  you can  redistribute   *
 * it and/or modify it under  terms of the  GNU General Public License as   *
 * published  by the  Free  Software  Foundation;  either  version 2,  or   *
 * (at your option)  any  later  version.  This benchmark is  distributed   *
 * in the hope that it will be useful, but WITHOUT ANY WARRANTY;  without   *
 * even  the  implied  warranty  of  MERCHANTABILITY  or  FITNESS  FOR  A   *
 * PARTICULAR  PURPOSE.   See the  GNU General  Public License  for  more   *
 * details.  You should have  received  a copy of the GNU General  Public   *
 * License  distributed with GNAT;  see file  COPYING.  If not, write  to   *
 * the Free Software Foundation, 59 Temple Place - Suite 330, Boston,  MA   *
 * 02111-1307, USA.                                                         *
 *                                                                          *
 * This benchmark was originally developed by ACT Europe and the Technical  *
 * University  of  Madrid (UPM) under  a contract funded  by  the European  *
 * Space (Statement of Work ref. TOS-EME/02-85/MRN)                         *
 *                                                                          *
 ****************************************************************************
*/



#include "support.h"
#include "support_rtems.h"



/******************************************************************
 *  The following variables are PRIVATE of the support package    *
 ******************************************************************/

int Simple_Random_State = 23;



/*
   -------------------------------------
   -- Internal Functions declarations --
   -------------------------------------
*/
bool R_Test_Sufficient_N_Of_Iterations (float *A, unsigned int len);
bool T_Test_Sufficient_N_Of_Iterations (float *A, unsigned int len);

void Sort (float *A, unsigned int len);
/* Sort in increase order a vector of floats (bubble algorithm is efficient
   --   for little vector (~ 20 elements))
*/

float Simple_Random ();
/*   --  Simple pseudo random number generator that is used in Proc_Spoil to
   --  inhibit optimization of the timing loop
*/

/* -----------------------------
   -- Jitter_Comfidence_Level --
   -----------------------------
*/

bool
Jitter_Confidence_Level (int Size, float Mean, float Sigma)
{
  return (T_Value[Size] * Sigma / (sqrt ((float) (Size)))) <= (Mean * 0.01);
}

void
Proc_Spoil ()
{

  if (Boolean_False)
    {
      Boolean_False = (Simple_Random_State != 0);
      Simple_Random_State = Simple_Random_State + 1000;
      Zero += (int) (Simple_Random);
      Max_NCount = Max_NCount + 1;
      Time_Flag = !Time_Flag;
      MCount++;
      NCount++;
      Count++;
      NTicks++;
      Elapsed_Time++;
      Time_Per_Tick++;
      Min_Time++;
      Standard_Error++;
      T_Statistic++;
      Null_Loop_Size++;
      Overall_Min_Time++;
      Overall_Max_Time++;
      Min_Jitter_Compensation++;
      Loop_Time++;
      Confidence_Interval_Within_Tolerance =
	!Confidence_Interval_Within_Tolerance;
      Timing_Mean++;
      Timing_Sigma++;
      Timing_Min++;
      Test_Time++;
      Max_Iteration_Count++;
      Min_Iteration_Count++;
      Excessive_Time++;
      Excessive_Time_Warning++;
    }
}



/*
   ---------------------------------------
   -- R_Test_Sufficient_N_Of_Iterations --
   ---------------------------------------
*/
bool
R_Test_Sufficient_N_Of_Iterations (float *A, unsigned int len)
{
  float *Temp = (float *) malloc (sizeof (float) * len);
  float Q1, Q3, Median;
  const int S = Max_Iteration_Count;	/*Lenght(Temp); */
  const int F = 0;		/*First(Temp); 0 */

  const int L = len - 1;
  memcpy (Temp, A, len * sizeof (float));

  Confidence_Interval_Within_Tolerance = False;

  /*      --  return false if we do not have a sufficient number of measure */
  if (L < Min_Iteration_Count)
    return False;

  Sort (Temp, len);

  /*    --  Calculate the 1st and 3rd quartiles using SAS method 5 */

  if ((S % 4) == 0)
    {
      Q1 = (Temp[F + S / 4 - 1] + Temp[F + S / 4]) / 2.0;
      Q3 = (Temp[L - S / 4] + Temp[L + 1 - S / 4]) / 2.0;
    }
  else
    {
      Q1 = Temp[(F + S / 4)];
      Q3 = Temp[(L - S / 4)];
    }


  /*      --  Get the median */
  if ((S % 2) == 1)
    {
      Median = Temp[F + S / 2];
    }
  else
    {
      Median = (Temp[F + S / 2 - 1] + Temp[F + S / 2]) / 2.0;
    }

  return
    T_Value[S] * (Q3 - Q1) / (1.075 * sqrt ((float) (S))) <
    Median * Timer_Tolerance;
}

/*
  -------------------------------------
  -- Significantly_Greater_Than_Zero --
  -------------------------------------
*/
bool
Significantly_Greater_Than_Zero (float Mean, float Sigma, int N)
{
  return (Mean - (T_Value[N - 1] * Sigma / sqrt ((float) (N)))) > 0.0;
}

/*
  -------------------
   -- Simple_Random --
   -------------------
*/
float
Simple_Random ()
{
  Simple_Random_State = (Simple_Random_State * 17) % 251;
  return (float) (Simple_Random_State) / 251.0;
}

/*
  ---------------------
  -- Spoil_Character --
  ---------------------
*/

void
Spoil_Character (char *C)
{
  *C = 'r';
}

void
Swap (int i, int j, float *V)
{
  float tmp = V[i];
  V[i] = V[j];
  V[j] = tmp;
}

/*Should be tested. */
void
Sort (float *V, unsigned int len)
{
  int i, j;
  /*      --  if Vector's length is 1 then there is nothing to do */
  /*uff    if V'Length = 1 then return; end if; */
  for (j = len - 1; j >= 0; j--)
    {
      for (i = 0; i <= j - 1; i++)
	{
	  if (V[i] > V[j])
	    {
	      Swap (i, j, V);
	    }
	}
    }
}

void
Standard_Dev (float *A, unsigned int len, float *Xba, float *Sigm)
{
  //  float Mean, T, Q ,R;
  //  int K;
  int i;
  /* DOESN't MAKE SENSE WITH STATIC VECTORS
     if A'Length = 1 then
     Xbar := A(A'First);
     end if;
   */

  /*      if A'Length <= 1 then
     Sigma := 0.0;
     return;
     end if;
   */
  *Xba = 0;
  *Sigm = 0;

  for (i = 0; i < len; i++)
    {
      *Xba += A[i];
      //      printf("time: %f\n", A[i]);
    }
  *Xba /= len;

  for (i = 0; i < len; i++)
    {
      *Sigm += pow2 (((A[i] - *Xba)));
      //        printf("__%f]] Xbar %f\n", *Sigm, pow2(((A[i] - *Xba))));
    }

  if (len != 1)
    *Sigm /= len - 1;

  //printf("[[%f]]\n", *Sigm);
  *Sigm = sqrt (*Sigm);
  //  printf("[[%f]]\n", *Sigm);


  /*S^2 cuasivar  Sigm /= MAXMEASURES -1; */

  /*      Mean := A(A'First);
     T := 0.0;
     K := 1;
     for I in A'First + 1 .. A'Last loop
     K := K + 1;
     Q := A(I) - Mean;
     R := Q / Float (K);
     Mean := Mean + R;
     T := T + Float (K - 1) * Q * R;
     end loop;

     Xbar := Mean;
     Sigma := Sqrt (T / Float (K - 1));
   */
}

bool
Sufficient_N_Of_Iterations (float *A, unsigned int len)
{

  if (T_Test_Sufficient_N_Of_Iterations (A, len))
    {
      Confidence_Interval_Within_Tolerance =
	(T_Test_Sufficient_N_Of_Iterations (A, len) ||
	 (MCount >= Max_Iteration_Count &&
	  T_Test_Sufficient_N_Of_Iterations (A, len)));
    }
  return Confidence_Interval_Within_Tolerance ||
    MCount >= Max_Iteration_Count;

}

bool
T_Test_Sufficient_N_Of_Iterations (float *A, unsigned int len)
{
  float Mean, Sigma;

  Confidence_Interval_Within_Tolerance = False;

  if (len < Min_Iteration_Count)
    return False;
  else
    {
      //  Compute t-statistic
      Standard_Dev (A, len, &Mean, &Sigma);
      Standard_Error = Sigma / (float) (sqrt ((float) (len)));
      return T_Value[MCount] * Standard_Error <= Mean * Timer_Tolerance;
    }
  return 0;
}

bool
Terminate_Timing_Loop ()
{
  bool Print_Unreliable_Indicator = False;

  Elapsed_Time = (float) (TF (Stop_Time) - TF (Start_Time)) -
    (float) (NTicks) * Estimated_System_Tick;	//Time_Per_Tick;

  Test_Time = Elapsed_Time / (float) (NCount) - Loop_Time;
  //printf ("Start %f Stop %f\n", TF(Start_Time), TF(Stop_Time));
  Test_Time = (Test_Time < 0.0 ? 0.0 : Test_Time);

  /* For debugging purposes only */
  printf ("Elapsed Total: %f Per test: %f Count %d Loop %f Nticks %d %f\n",
	  Elapsed_Time,
	  Test_Time, NCount, Loop_Time, NTicks, Estimated_System_Tick);

  if (!Time_Flag)		// Good NCount has not been found until now
    {

      if (((Time_Per_Tick / (float) (NCount) < Test_Time * Timer_Tolerance &&
	    Elapsed_Time > Min_Jitter_Compensation))
	  || (NCount >= Max_NCount))
	{
	  Min_Time = Test_Time;
	  Time_Flag = True;
	}
      else
	NCount = NCount * 2 + 1;
    }

  if (Time_Flag)		// Good NCount has been encountered
    {
      if ((NCount < Max_NCount) &&
	  (Test_Time < Min_Time / Excessive_Variability ||
	   Test_Time > Min_Time * Excessive_Variability))
	{
	  if (((float) (NCount) * Max (Min_Time, Test_Time) >
	       Excessive_Variability_Min_Time)
	      && (Elapsed_Time > Min_Jitter_Compensation))
	    {
	      if (MCount > Min_Iteration_Count)
		{
		  Timing_Vector[MCount] = Test_Time;
		  MCount = MCount + 1;
		  Min_Time = min (Min_Time, Test_Time);
		  return True;
		}
	      else
		{
		  Time_Flag = False;
		  NCount = NCount * 2 + 1;
		  MCount = 0;
		}
	    }

	  Min_Time = min (Min_Time, Test_Time);

	  if (Time_Flag)	// Inner Loop has not been extended
	    {
	      Timing_Vector[MCount] = Test_Time;
	      MCount = MCount + 1;
	      if (Sufficient_N_Of_Iterations (Timing_Vector, MCount) ||
		  (Min_Time <= 0.0 && MCount >= Min_Iteration_Count))
		{
		  return True;
		}
	    }
	}

      GETCLKSEC (End_Time);

      if ((float) (End_Time - Begin_Time) > Excessive_Time)
	{
	  return True;
	}
      else if ((float) (End_Time - Begin_Time) > Excessive_Time_Warning)
	{
	  Standard_Dev (Timing_Vector, MCount, &Timing_Mean, &Timing_Sigma);
	  if (Timing_Min != 0.0)
	    if (Confidence_Interval_Within_Tolerance)
	      Print_Unreliable_Indicator = True;

	  //  Output Measurement
	  //delay 0.5;
	  return False;
	}
      else
	return False;
    }

}

void
Test_End ()
{
  enum Message M = Null_Msg;

  if (Min_Time < 0.0)
    {
      /*  Handle case of negative value */
      if (abs (Min_Time) < abs (Overall_Max_Time - Overall_Min_Time))
	{
	  M = Noise_Msg;
	  Min_Time = 0.0;
	}
      else
	{
	  M = Negative_Time_Msg;
	}
    }

  Standard_Dev (Timing_Vector, MCount, &Timing_Mean, &Timing_Sigma);
  Put_Measure (Min_Time, Timing_Mean, Timing_Sigma, M);

}

bool
Decrease_Counter ()
{

  //  printf("Decrease counter: %d\n", Count);
  if (Count < Zero)
    {
      Proc_Spoil ();
    }
  Count--;
  if (Count <= Zero)
    return True;
  else
    return False;
}

void
Set_Start_Time ()
{
  GETTIME (S_Time);
  do
    {
      GETTIME (Start_Time);

    }
  while (Start_Time.microseconds == S_Time.microseconds);
}

void
Set_Stop_Time ()
{
  GETTIME (S_Time);
  do
    {
      GETTIME (Stop_Time);
      NTicks++;			// Vernier Ticks
    }
  while (Stop_Time.microseconds == S_Time.microseconds);

}





/* Extern variables which are owned by this package */

/* DUAL LOOP var initializations */
bool Time_Flag = False;
int NCount = 1;
int MCount = 1;
int NTicks = 0;
float Begin_Time = 0.0;
float End_Time = 0.0;
int Count = 0;
int Zero = 0;
float Test_Time = 0.0;
int Number_Of_Clock_Ticks_In_One_Second = 1;


/*   --  Table for the Student T test (for 90% confidence level) */
float T_Value[] = { 1.0000, 6.3138, 2.9200, 2.3534, 2.1318,
  2.0150, 1.9432, 1.8946, 1.8595, 1.8331,
  1.8125, 1.7959, 1.7823, 1.7709, 1.7613,
  1.7530, 1.7459, 1.7396, 1.7341, 1.7291
};

/* 20 values */

int Integer_One = 1;
float Float_01 = 1.33333;

float Min_Time;
float Overall_Min_Time, Overall_Max_Time;
bool Confidence_Interval_Within_Tolerance;

float Time_Per_Tick = 0.0;
rtems_clock_time_value S_Time, Start_Time, Stop_Time;
float Timing_Mean, Timing_Min, Timing_Sigma;
char Boolean_False = False;
int MAX_NCount = 2097151; /* pow isn't a good idea. Shift? */
int Min_Iteration_Count = 10; /* Minimum number of measures */
int Max_Iteration_Count = 19; /* Maximum number of measures */
int Excessive_Time = 1800; /* Half an hour Maximum whole test duration */
int Excessive_Time_Warning = 300;	/* Not used for the moment */
float Timing_Vector[100];
int Count; /*   --  Iteration counter. */
float Test_Time;
float Elapsed_Time, Min_Time;
int Number_Of_Clock_Ticks_In_One_Second;
bool Confidence_Interval_Within_Tolerance;
float Loop_Time;
float Min_Jitter_Compensation;
float Overall_Min_Time, Overall_Max_Time;
float T_Statistic; /* Computed T Value */
float Null_Loop_Size;
float Standard_Error; /*  */
int Max_NCount = 2097151;
float Measured_System_Tick, Measured_Sigma;
float Estimated_System_Tick, Quantization_Tolerance;
