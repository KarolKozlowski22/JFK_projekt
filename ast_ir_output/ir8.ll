; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.4593572070920732383" = internal constant [3 x i8] c"%d\00"
@".str.1495783277522668851" = internal constant [3 x i8] c"%f\00"
@".str.966308075288711710" = internal constant [3 x i8] c"%s\00"
@".str.8146335450369478114" = internal constant [2 x i8] c"\0a\00"
define void @"main"()
{
entry:
  %".2" = sdiv i32 7, 2
  %"b" = alloca i32
  store i32 %".2", i32* %"b"
  %".4" = sitofp i32 2 to float
  %".5" = fdiv float 0x401c000000000000, %".4"
  %"c" = alloca float
  store float %".5", float* %"c"
  %".7" = load i32, i32* %"b"
  %".8" = bitcast [2 x i8]* @".str.8146335450369478114" to i8*
  %".9" = bitcast [3 x i8]* @".str.4593572070920732383" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".7")
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".8")
  %".12" = load float, float* %"c"
  %".13" = bitcast [2 x i8]* @".str.8146335450369478114" to i8*
  %".14" = bitcast [3 x i8]* @".str.1495783277522668851" to i8*
  %".15" = fpext float %".12" to double
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".14", double %".15")
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".13")
  ret void
}
