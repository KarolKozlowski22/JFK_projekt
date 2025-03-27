; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.-2452015952092396623" = private constant [4 x i8] c"%d\0a\00"
@".str.-774703926669740791" = private constant [4 x i8] c"%f\0a\00"
define void @"main"()
{
entry:
  %".2" = add float 0x4000000000000000, 0x4008000000000000
  %".3" = mul float 0x4014000000000000, %".2"
  store float %".3", float* @"x"
  %".5" = load float, float* @"x"
  %".6" = bitcast [4 x i8]* @".str.-774703926669740791" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", float %".5")
  ret void
}

@"x" = global float              0x0