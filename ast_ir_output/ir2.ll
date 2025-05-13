; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.8372795069725211921" = internal constant [3 x i8] c"%d\00"
@".str.170774002489608625" = internal constant [3 x i8] c"%f\00"
@".str.3693790085204977514" = internal constant [3 x i8] c"%s\00"
@".str.332649807079450794" = internal constant [2 x i8] c"\0a\00"
define void @"main"()
{
entry:
  %".2" = sitofp i32 2 to float
  %".3" = fmul float 0x400c000000000000, %".2"
  %".4" = sitofp i32 10 to float
  %".5" = fadd float %".4", %".3"
  %"a" = alloca float
  store float %".5", float* %"a"
  %".7" = load float, float* %"a"
  %".8" = bitcast [2 x i8]* @".str.332649807079450794" to i8*
  %".9" = bitcast [3 x i8]* @".str.170774002489608625" to i8*
  %".10" = fpext float %".7" to double
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".9", double %".10")
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".8")
  ret void
}
